from application.crud.snapshot import generate_session, upload_chunk
from fastapi import APIRouter, File, UploadFile


router = APIRouter()

@router.post("/{world_id}/snapshots/upload")
async def intiate_session(world_id: str, name: str):
    return generate_session(world_id=world_id, name=name)


@router.post("/{world_id}/snapshots/upload/{session_id}")
async def upload_session_chunk(
    world_id: str,
    session_id: str,
    name: str,
    part: int = 1,
    file: UploadFile = File(...)):
    
    return upload_chunk(
        world_id=world_id,
        session_id=session_id,
        name=name,
        part=part,
        file=file
    )
