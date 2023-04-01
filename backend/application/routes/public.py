from application.crud.public import download_shared_world, grab_shared_world
from fastapi import APIRouter, Path, Query


router = APIRouter()


@router.get("/worlds/{world_id}")
async def get_world_by_id(
    world_id: str = Path(..., description="The unique identifier of the world.")
):
    return grab_shared_world(world_id)


@router.get("/worlds/{world_id}/download")
async def download_world_by_part(
    world_id: str = Path(..., description="The unique identifier of the world."),
    part: int = Query(1, description="The part number of the uploaded file."),
):
    return download_shared_world(world_id, part)
