import time
from application.utils.connections import upload_session_db, worlds_db, snapshot_db, shard_drive

from fastapi import UploadFile, File, HTTPException, status

from nanoid import generate

def generate_session(world_id: str, name: str):
    
    try:
        world = worlds_db.get(world_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    if not world:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    snapshot_id = generate()
    
    current_time = int(time.time())
    
    try:
        snapshot_db.put({
            "world_id": world_id,
            "name": f"{current_time}-{snapshot_id}",
            "parts": 0,
            "size": 0,
            "created_at": current_time
        }, snapshot_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    try:
        session = upload_session_db.put({
            "snapshot_id": snapshot_id,
            "world_id": world_id,
            "name": name,
            "current_part": 0,
            "current_size": 0
        })
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return session

async def upload_chunk(
    world_id: str,
    session_id: str,
    name: str,
    part: int = 1,
    file: UploadFile = File(...)):
    
    try:
        session = upload_session_db.get(session_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    if not session["world_id"] == world_id: # type: ignore
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
    if not session["name"] == name: # type: ignore
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
    if not session["part"] < part: # type: ignore
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED)
    
    snapshot = snapshot_db.get(session["snapshot_id"]) # type: ignore  
      
    if not snapshot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    file_size = len(await file.read())
    
    await file.seek(0)
    
    shard_drive.put(f"{snapshot['name']}.part{part}", file.read()) # type: ignore
    
    upload_session_db.update({
        "parts": session["part"] + 1, # type: ignore
        "size": session["size"] + file_size # type: ignore
        
    }, session_id) # type: ignore
    