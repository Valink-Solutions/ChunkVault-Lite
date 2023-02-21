import os
import time
from typing import Union
from fastapi import APIRouter, UploadFile, File, Header, HTTPException, status
from fastapi.responses import JSONResponse
from nanoid import generate

from application.utils.databases import snapshot_db, snapshot_drive, upload_session_db, worlds_db

router = APIRouter()

@router.post("/")
async def upload_snapshot(file: UploadFile, world_id: str, file_name: str, session_id: str = None, content_length: int = 0):
    
    world = worlds_db.get(world_id)
    
    if not world:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"World: {world_id} does not exist.")
    
    if not session_id:
        session =  upload_session_db.put({"name": file_name, "size": 0, "total_size": content_length})
        session_id = session["key"]
    else:
        session = upload_session_db.get(session_id)
        if session is None:
            return JSONResponse({"error": "Session not found"}, status_code=404)
        if session["name"] != file_name:
            return JSONResponse({"error": "Filename does not match session"}, status_code=400)

    chunk = await file.read()
    
    with open(f"./tmp/{session_id}.part", "ab") as f:
        f.write(chunk)
        
    session_size = session["size"] + len(chunk)
    
    upload_session_db.update({"size": session_size}, session_id)
    
    if session_size == session["total_size"]:
        
        with open(f"./tmp/{session_id}.part", "rb") as f:
            snapshot_drive.put(f"{world_id}/{session['name']}", f)
            
            snapshot_db.put({"world_id": world_id, "name": f"{world_id}/{session['name']}", "size": content_length, "created_at": time.time()})
            
            worlds_db.update({"num_snapshots": world["num_snapshots"]+1}, world["key"])
            
        upload_session_db.delete(session_id)
        
        os.remove(f"./tmp/{session_id}.part")
        
        return JSONResponse({"session_id": session_id, "finished": True})
        
    return JSONResponse({"session_id": session_id, "finished": False})

@router.get("/")
async def get_snapshots(last: str = None, limit: int = 100):
    results = snapshot_db.fetch(limit=limit, last=last)
    
    return results

@router.get("/{snapshot_id}")
async def get_snapshot(snapshot_id: str, download: bool = False):
    snapshot_data = snapshot_db.get(snapshot_id)
    
    if not snapshot_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Snapshot {snapshot_id} does not exist.")
    
    if not download:
        return JSONResponse(content=snapshot_data)
    
    return snapshot_drive.get(snapshot_data["name"])