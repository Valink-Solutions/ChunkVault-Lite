from typing import Union
from application.schemas.world import NewWorldSchema, UpdateWorldSchema, WorldSchema
from application.utils import remove_none_values
from application.utils.connections import (
    worlds_db,
    snapshot_db,
    shard_drive,
    shared_worlds_db,
    deleted_snapshots_db,
)

from fastapi import BackgroundTasks, HTTPException, status
from fastapi.responses import JSONResponse


def create_world(world_data: NewWorldSchema, suggested_key: Union[str, None] = None):
    new_world = WorldSchema(**world_data.dict())

    if suggested_key:
        results = worlds_db.get(suggested_key)

        if results:  # type: ignore
            return HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail=f"World: {new_world.name} already exists.",
            )

        result = worlds_db.put(new_world.dict(), suggested_key)
    else:
        result = worlds_db.put(new_world.dict())

    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse(content=result)


def get_world(world_id: str):
    world = worlds_db.get(world_id)

    if not world:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return world


def get_world_snapshots(world_id: str, last: Union[str, None] = None, limit: int = 100):
    world = worlds_db.get(world_id)

    if not world:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    results = snapshot_db.fetch(
        {"world_id": world_id}, last=last, limit=limit  # type: ignore
    )

    return {"count": results.count, "last": results.last, "items": results.items}


def get_worlds(last: Union[str, None] = None, limit: int = 100):
    results = worlds_db.fetch(last=last, limit=limit)  # type: ignore

    if not results.count > 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(
        content={"count": results.count, "last": results.last, "items": results.items}
    )


def update_world(world_id: str, world_data: UpdateWorldSchema):
    world = worlds_db.get(world_id)

    if not world:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"World: {world_id} does not exist.",
        )

    parsed_data = remove_none_values(world_data.dict())

    if parsed_data.get("is_public") is True:
        shared_worlds_db.put({"world_id": world["key"]})  # type: ignore
    else:
        shared_resp = shared_worlds_db.fetch({"world_id": world["key"]})  # type: ignore

        if shared_resp.count > 0:
            shared_worlds_db.delete(shared_resp.items[0]["key"])  # type: ignore

    try:
        worlds_db.update(parsed_data, world["key"])  # type: ignore
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"World: {world_id} could not be updated.",
        )

    return JSONResponse(status_code=200, content=f"World: {world_id} was updated.")


async def delete_world(world_id: str, background_tasks: BackgroundTasks):
    world = worlds_db.get(world_id)

    if not world:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"World: {world_id} does not exist.",
        )

    try:
        worlds_db.delete(world_id)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail=f"World: {world_id} could not be deleted.",
        )

    background_tasks.add_task(delete_world_snapshots, world_id, background_tasks)

    return JSONResponse(status_code=200, content=f"World: {world_id} was deleted.")


async def delete_world_snapshots(world_id: str, background_tasks: BackgroundTasks):
    results = snapshot_db.fetch({"world_id": world_id})

    final_snaps = results.items

    while results.last:
        results = snapshot_db.fetch({"world_id": world_id}, last=results.last)

        final_snaps += results.last

    for result in final_snaps:
        try:
            snapshot_db.delete(result["key"])
        except Exception:
            pass

        deleted_snapshots_db.put(
            {
                "snapshot_id": result["key"],
                "name": result["name"],
                "parts": result["parts"],
            }
        )

        background_tasks.add_task(
            delete_snapshot_pieces, f'{result["key"]}/{result["name"]}', result["parts"]
        )


async def delete_snapshot_pieces(snapshot_id: str, parts: int):
    for part in range(parts):
        try:
            shard_drive.delete(f"{snapshot_id}.part{part+1}")
        except Exception:
            pass
