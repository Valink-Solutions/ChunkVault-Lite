from typing import Union

# from application.crud.snapshot import (
#     abort_session,
#     finish_session,
#     generate_session,
#     upload_chunk,
# )
from application.crud.world import (
    create_world,
    delete_world,
    get_world,
    get_worlds,
    update_world,
)
from application.schemas.world import NewWorldSchema, UpdateWorldSchema

from fastapi import APIRouter, Body


router = APIRouter()


@router.get("")
async def grab_worlds(last: Union[str, None] = None, limit: int = 100):
    return get_worlds(last, limit)


@router.post("")
async def create_new_world(
    suggested_key: Union[str, None] = None, world_data: NewWorldSchema = Body(...)
):
    return create_world(suggested_key=suggested_key, world_data=world_data)


@router.get("/{world_id}")
async def grab_world_by_id(world_id: str):
    return get_world(world_id=world_id)


@router.patch("/{world_id}")
async def update_world_by_id(world_id: str, world_data: UpdateWorldSchema = Body(...)):
    return update_world(world_id, world_data)


@router.delete("/{world_id}")
async def delete_world_by_id(world_id: str):
    return delete_world(world_id)


# World Snapshot options

# @router.post("/{world_id}/snapshots/upload", tags=["Snapshot Managment"])
# async def intiate_session(world_id: str, name: str, size: int):
#     return generate_session(world_id=world_id, name=name, size=size)


# @router.post("/{world_id}/snapshots/upload/{session_id}", tags=["Snapshot Managment"])
# async def upload_session_chunk(
#     world_id: str,
#     session_id: str,
#     name: str,
#     part: int = 1,
#     file: UploadFile = File(...),
# ):
#     return await upload_chunk(
#         world_id=world_id, session_id=session_id, name=name, part=part, file=file
#     )


# @router.patch(
# "/{world_id}/snapshots/upload/{session_id}",
# tags=["Snapshot Managment"]
# )
# async def end_upload_session(world_id: str, session_id: str, name: str):
#     return finish_session(world_id=world_id, session_id=session_id, name=name)


# @router.delete(
#     "/{world_id}/snapshots/upload/{session_id}",
#     tags=["Snapshot Managment"]
# )
# async def abort_upload_session(world_id: str, session_id: str, name: str):
#     return abort_session(world_id=world_id, session_id=session_id, name=name)
