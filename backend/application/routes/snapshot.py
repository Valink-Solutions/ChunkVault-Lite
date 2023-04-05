from typing import Union

from application.crud.snapshot import (
    abort_session,
    create_snapshot,
    delete_snapshot,
    finish_session,
    generate_session,
    grab_snapshot,
    grab_snapshots,
    upload_chunk,
    download_snapshot_part,
    snapshot_size_on_disk,
)

from application.schemas.snapshot import NewSnapshotSchema
from fastapi import APIRouter, Body, File, Path, Query, UploadFile, BackgroundTasks


router = APIRouter()


@router.get(
    "",
    summary="Fetch snapshots",
    description="""
Fetches set of snapshots based on limit and last item key.
last key will start the fetch at that items index.
""",
)
async def get_snapshots(
    last: Union[str, None] = Query(None, description="The starting key for the fetch."),
    limit: int = Query(100, description="The item return limit."),
):
    return grab_snapshots(last=last, limit=limit)


@router.post(
    "",
    summary="Create a new snapshot",
    description="""
Allows for the creation of a new snapshot.
""",
)
async def create_new_snapshot(data: NewSnapshotSchema = Body(...)):
    return create_snapshot(data.world_id, data.size)


@router.get(
    "/info/",
    summary="Grab snapshot info",
    description="""
Returns the total size and number of all snapshots.
""",
)
async def grab_snapshots_info():
    return snapshot_size_on_disk()


@router.delete(
    "/{snapshot_id}",
    summary="Delete snapshot by ID",
    description="""
Allows deletion of snapshot and all related files via ID.
""",
)
async def delete_snapshot_by_id(
    background_tasks: BackgroundTasks,
    snapshot_id: str = Path(..., description="The unique identifier of the snapshot."),
):
    return await delete_snapshot(snapshot_id)


@router.get(
    "/{snapshot_id}",
    summary="Grab snapshot by ID",
    description="""
Returns the entire snapshot data.
""",
)
async def get_snapshot_by_id(
    snapshot_id: str = Path(..., description="The unique identifier of the snapshot.")
):
    return grab_snapshot(snapshot_id)


@router.get(
    "/{snapshot_id}/download",
    summary="Fetch snapshot part by ID",
    description="""
Returns the raw chunk data of the snapshot file specified by the part.
""",
)
async def download_snapshot_by_id(
    snapshot_id: str = Path(..., description="The unique identifier of the snapshot."),
    part: int = Query(1, description="The part number of the uploaded file."),
):
    return download_snapshot_part(snapshot_id=snapshot_id, part=part)


@router.post(
    "/{snapshot_id}/session",
    summary="Create an upload session",
    description="""
This route allows users to create an upload session for a snapshot.
""",
)
async def get_session(
    snapshot_id: str = Path(..., description="The unique identifier of the snapshot."),
    name: str = Query(..., description="The name of the uploaded file."),
):
    return generate_session(snapshot_id, name)


@router.post(
    "/{snapshot_id}/session/{session_id}/upload",
    summary="Upload a snapshot part",
    description="""
This route allows users to upload a snapshot part.
Each snapshot part is associated with a specific snapshot ID and session ID.
""",
)
async def upload_snapshot_part(
    snapshot_id: str = Path(..., description="The unique identifier of the snapshot."),
    session_id: str = Path(..., description="The unique identifier of the session."),
    name: str = Query(..., description="The name of the uploaded file."),
    part: int = Query(1, description="The part number of the uploaded file."),
    file: UploadFile = File(..., description="The file to be uploaded."),
):
    return await upload_chunk(
        snapshot_id=snapshot_id, session_id=session_id, name=name, part=part, file=file
    )


@router.patch(
    "/{snapshot_id}/session/{session_id}/upload",
    summary="End upload session",
    description="""
Cleans up message que and ensures snapshot creation.
""",
)
async def end_upload_session(
    snapshot_id: str = Path(..., description="The unique identifier of the snapshot."),
    session_id: str = Path(..., description="The unique identifier of the session."),
    name: str = Query(..., description="The name of the uploaded file."),
):
    return finish_session(session_id=session_id, name=name)


@router.delete(
    "/{snapshot_id}/session/{session_id}/upload",
    summary="Quit an upload sesison",
    description="""
Removes all uploaded parts and cleans up message que/
""",
)
async def abort_upload_session(
    snapshot_id: str = Path(..., description="The unique identifier of the snapshot."),
    session_id: str = Path(..., description="The unique identifier of the session."),
    name: str = Query(..., description="The name of the uploaded file."),
):
    return abort_session(session_id=session_id, name=name)
