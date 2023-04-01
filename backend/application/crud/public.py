from application.utils.connections import (
    worlds_db,
    shared_worlds_db,
    snapshot_db,
    shard_drive,
)
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse, Response


def create_new_shared_world(world_id: str):
    world = worlds_db.get(world_id)

    if world["is_public"]:  # type: ignore
        return JSONResponse(content={"message": "World already shared."})

    worlds_db.update({"is_public": True}, world["key"])  # type: ignore

    shared_worlds_db.put({"world_id": world["key"]})  # type: ignore

    response = shared_worlds_db.fetch({"world_id": world["key"]})  # type: ignore

    if response.count <= 0:
        raise HTTPException(status_code=500)

    return {"key": response.items[0]["key"]}


def grab_shared_world(shared_id: str):
    shared_world = shared_worlds_db.get(shared_id)

    if not shared_world:
        raise HTTPException(status_code=404)

    world_key = shared_world["world_id"]  # type: ignore

    world = worlds_db.get(world_key)

    if not world:
        raise HTTPException(status_code=404)

    latest_snap = snapshot_db.get(world["newest_snapshot"])  # type: ignore

    del world["key"]  # type: ignore
    del world["newest_snapshot"]  # type: ignore
    world["full_size"] = world["size"]  # type: ignore
    del world["size"]  # type: ignore

    del latest_snap["key"]  # type: ignore
    del latest_snap["name"]  # type: ignore
    del latest_snap["world_id"]  # type: ignore

    data = {
        "key": shared_id,
        **world,  # type: ignore
        **latest_snap,  # type: ignore
    }

    return data


def get_shared_world(world_id: str):
    response = shared_worlds_db.fetch({"world_id": world_id})

    if response.count <= 0:
        raise HTTPException(status_code=404)

    return {"key": response.items[0]["key"]}


def download_shared_world(shared_id: str, part: int):
    shared_world = shared_worlds_db.get(shared_id)

    if not shared_world:
        raise HTTPException(status_code=404)

    world_key = shared_world["world_id"]  # type: ignore

    world = worlds_db.get(world_key)

    if not world:
        raise HTTPException(status_code=404)

    snapshot = snapshot_db.get(world["newest_snapshot"])  # type: ignore

    snapshot_id = snapshot["key"]  # type: ignore

    if not snapshot:
        raise HTTPException(
            status_code=404,
            detail={"message": "Snapshot does not exist."},
        )

    try:
        file = shard_drive.get(
            f"{snapshot_id}/{snapshot['name']}.part{part}"  # type: ignore
        )
    except Exception:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

    if not file:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

    return Response(file.read(), media_type="application/zip")
