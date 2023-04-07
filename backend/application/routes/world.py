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

from fastapi import APIRouter, BackgroundTasks, Body, Path, Query


router = APIRouter()


@router.get(
    "",
    summary="Fetch Worlds",
    description="""
Fetches set of worlds based on limit and last item key.
last key will start the fetch at that items index.
""",
)
async def grab_worlds(
    last: Union[str, None] = Query(None, description="The starting key for the fetch."),
    limit: int = Query(100, description="The item return limit."),
):
    return get_worlds(last, limit)


@router.post(
    "",
    summary="Create a new world",
    description="""
This route creates a new world with the given data. You can either provide a suggested
key to set as the world ID or let the system generate one.
""",
)
async def create_new_world(
    suggested_key: Union[str, None] = Query(
        None,
        description="""
If provided, this value will be used as the world ID
instead of generating one automatically.
""",
    ),
    world_data: NewWorldSchema = Body(
        ...,
        description="""
A JSON object containing the necessary data to create a new world.
""",
    ),
):
    return create_world(suggested_key=suggested_key, world_data=world_data)


@router.get(
    "/{world_id}",
    summary="Grab world by ID",
    description="""
Returns the JSON object representing the world.    
""",
)
async def grab_world_by_id(
    world_id: str = Path(..., description="The unique identifier of the world.")
):
    return get_world(world_id=world_id)


@router.get(
    "/{world_id}/snapshots",
    summary="Fetch World snapshots",
    description="""
Fetches set of world's snapshots based on limit and last item key.
last key will start the fetch at that items index.
""",
)
async def grab_world_snapshots_by_id(
    world_id: str = Path(..., description="The unique identifier of the world."),
    last: Union[str, None] = Query(None, description="The starting key for the fetch."),
    limit: int = Query(100, description="The item return limit."),
):
    return get_world_snapshots(world_id=world_id, last=last, limit=limit)


@router.patch(
    "/{world_id}",
    summary="Update a world by ID",
    description="This route updates the specified world with the provided data.",
)
async def update_world_by_id(
    world_id: str = Path(..., description="The unique identifier of the world."),
    world_data: UpdateWorldSchema = Body(
        ..., description="The updated data for the world."
    ),
):
    return update_world(world_id, world_data)


@router.delete(
    "/{world_id}",
    summary="Delete a world by ID",
    description="This route deletes the specified world.",
)
async def delete_world_by_id(
    background_tasks: BackgroundTasks,
    world_id: str = Path(..., description="The unique identifier of the world."),
):
    return await delete_world(world_id, background_tasks)
