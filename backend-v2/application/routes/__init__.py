from application.routes import snapshot, world

from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/health_check")
async def get_health_status():
    return JSONResponse(
        status_code=200, content={"message": "ChunkVault - Lite is online!"}
    )


router.include_router(snapshot.router, prefix="/snapshots")
router.include_router(world.router, prefix="/worlds")
