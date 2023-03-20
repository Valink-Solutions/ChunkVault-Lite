from typing import Union

from application.crud.world import (
    create_world,
    delete_world,
    get_world,
    get_world_snapshots,
    get_worlds,
    update_world,
)
from application.schemas.world import NewWorldSchema, UpdateWorldSchema

from fastapi import APIRouter, BackgroundTasks, Body


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


@router.get("/{world_id}/snapshots")
async def grab_world_snapshots_by_id(
    world_id: str, last: Union[str, None] = None, limit: int = 100
):
    return get_world_snapshots(world_id=world_id, last=last, limit=limit)


@router.patch("/{world_id}")
async def update_world_by_id(world_id: str, world_data: UpdateWorldSchema = Body(...)):
    return update_world(world_id, world_data)


@router.delete("/{world_id}")
async def delete_world_by_id(world_id: str, background_tasks: BackgroundTasks):
    return await delete_world(world_id, background_tasks)
