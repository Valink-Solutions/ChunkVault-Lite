from typing import Union

from application.crud.snapshot import (
    abort_session,
    create_snapshot,
    finish_session,
    generate_session,
    grab_snapshot,
    grab_snapshots,
    upload_chunk,
    download_snapshot_part,
    download_full_snapshot,
    snapshot_size_on_disk,
)

from application.schemas.snapshot import NewSnapshotSchema
from fastapi import APIRouter, Body, File, UploadFile


router = APIRouter()


@router.get("")
async def get_snapshots(last: Union[str, None] = None, limit: int = 100):
    return grab_snapshots(last=last, limit=limit)


@router.post("")
async def create_new_snapshot(data: NewSnapshotSchema = Body(...)):
    return create_snapshot(data.world_id, data.size)


@router.get("/info/")
async def grab_snapshots_info():
    return snapshot_size_on_disk()


@router.get("/{snapshot_id}")
async def get_snapshot_by_id(snapshot_id: str):
    return grab_snapshot(snapshot_id)


@router.get("/{snapshot_id}/download")
async def download_snapshot_by_id(snapshot_id: str, part: int = 1):
    return download_snapshot_part(snapshot_id=snapshot_id, part=part)


@router.get("/{snapshot_id}/download_full")
async def download_full_snapshot_by_id(snapshot_id: str):
    return download_full_snapshot(snapshot_id=snapshot_id)


@router.post("/{snapshot_id}/session")
async def get_session(snapshot_id: str, name: str):
    return generate_session(snapshot_id, name)


@router.post("/{snapshot_id}/session/{session_id}/upload")
async def upload_snapshot_part(
    snapshot_id: str,
    session_id: str,
    name: str,
    part: int = 1,
    file: UploadFile = File(...),
):
    return await upload_chunk(
        snapshot_id=snapshot_id, session_id=session_id, name=name, part=part, file=file
    )


@router.patch("/{snapshot_id}/session/{session_id}/upload")
async def end_upload_session(snapshot_id: str, session_id: str, name: str):
    return finish_session(session_id=session_id, name=name)


@router.delete("/{snapshot_id}/session/{session_id}/upload")
async def abort_upload_session(snapshot_id: str, session_id: str, name: str):
    return abort_session(session_id=session_id, name=name)
