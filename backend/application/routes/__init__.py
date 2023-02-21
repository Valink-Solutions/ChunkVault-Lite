from fastapi import APIRouter

from application.routes import snapshots

router = APIRouter()

router.include_router(snapshots.router, prefix="/snapshots")