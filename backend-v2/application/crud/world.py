from typing import Union
from application.schemas.world import NewWorldSchema, UpdateWorldSchema, WorldSchema
from application.utils import remove_none_values
from application.utils.connections import worlds_db

from fastapi import HTTPException, status
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

    try:
        worlds_db.update(parsed_data, world["key"])  # type: ignore
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"World: {world_id} could not be updated.",
        )

    return JSONResponse(status_code=200, content=f"World: {world_id} was updated.")


def delete_world(world_id: str):
    return world_id
