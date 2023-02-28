from fastapi import APIRouter

from application.routes import snapshots, worlds

router = APIRouter()

router.include_router(snapshots.router, prefix="/snapshots", tags=["snapshots"])
router.include_router(worlds.router, prefix="/worlds", tags=["worlds"])
