from application.routes import snapshot, world, public, actions

from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/health_check")
async def get_health_status():
    return JSONResponse(
        status_code=200, content={"message": "ChunkVault - Lite is online!"}
    )


router.include_router(snapshot.router, prefix="/snapshots", tags=["Snapshot Managment"])
router.include_router(world.router, prefix="/worlds", tags=["World Managment"])
router.include_router(public.router, prefix="/public", tags=["Public Endpoints"])
router.include_router(
    actions.router, prefix="/__space/v0/actions", tags=["Scheduled Actions"]
)
