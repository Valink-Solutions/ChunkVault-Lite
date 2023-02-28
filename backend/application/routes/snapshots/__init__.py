import io
import time
from fastapi import APIRouter, UploadFile, Header, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse

from application.utils.databases import (
    snapshot_db,
    snapshot_drive,
    upload_session_db,
    worlds_db,
    temp_drive,
)

router = APIRouter()


@router.post("/upload")
async def initiat_snapshot_session(file_name: str, world_id: str):
    world = worlds_db.get(world_id)

    if not world:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"World: {world_id} does not exist.",
        )

    session = upload_session_db.put(
        {"name": file_name, "world_id": world_id, "last_chunk": 0}, expire_in=1800
    )

    if not session:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    session_id = session["key"]

    return JSONResponse(content={"session_id": session_id})


@router.post("/upload/{session_id}")
async def upload_snapshot(
    file: UploadFile, session_id: str, file_name: str, content_range: str = Header(...)
):
    start_current, total = content_range.split()[1].split("/")
    start, current = start_current.split("-")
    start, current, total = int(start), int(current), int(total)

    session = upload_session_db.get(session_id)

    if session is None:
        return JSONResponse({"error": "Session not found"}, status_code=404)
    if session["name"] != file_name:
        return JSONResponse(
            {"error": "Filename does not match session"}, status_code=400
        )
    if current <= session["last_chunk"]:
        return JSONResponse(
            {"error": "Chunk already written"},
            status_code=status.HTTP_208_ALREADY_REPORTED,
        )

    new_temp_file = io.BytesIO()

    chunk = await file.read()

    files = temp_drive.list(prefix=f"{session_id}")

    temp_file_exists = (
        files["names"] if files["names"] == f"{session_id}.part" else None
    )

    if not temp_file_exists:
        new_temp_file.write(chunk)

        new_temp_file.seek(0)
        try:
            temp_drive.put(f"{session_id}.part", new_temp_file)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        temp_file = temp_drive.get(f"{session_id}.part")

        for part in temp_file.iter_chunks():
            new_temp_file.write(part)

        temp_file.close()

        new_temp_file.seek(0)

        new_temp_file.seek(start)

        new_temp_file.write(chunk)

        new_temp_file.seek(0)

        temp_drive.put(f"{session_id}.part", new_temp_file)

    upload_session_db.update({"last_chunk": current}, session_id)

    if current >= total:
        world = worlds_db.get(session["world_id"])

        if not world:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"World: {session['world_id']} does not exist.",
            )

        world_id = world["key"]

        current_time = int(time.time())

        session_file = temp_drive.get(f"{session_id}.part")

        snapshot_name = f"{current_time}-snapshot.{session['name'].split('.')[1]}"

        snapshot_drive.put(f"{world_id}/{snapshot_name}", session_file.read())

        session_file.close()

        snapshot_db.put(
            {
                "world_id": world_id,
                "name": f"{snapshot_name}",
                "size": total,
                "created_at": time.time(),
            }
        )

        worlds_db.update({"num_snapshots": world["num_snapshots"] + 1}, world["key"])

        upload_session_db.delete(session_id)

        temp_drive.delete(f"{session_id}.part")

        return JSONResponse({"session_id": session_id, "finished": True})

    return JSONResponse({"session_id": session_id, "finished": False})


@router.get("/")
async def get_snapshots(last: str = None, limit: int = 100):
    results = snapshot_db.fetch(limit=limit, last=last)

    if not results.count > 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {"count": results.count, "last": results.last, "items": results.items}


@router.get("/{snapshot_id}")
async def get_snapshot(snapshot_id: str, download: bool = False):
    snapshot_data = snapshot_db.get(snapshot_id)

    if not snapshot_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Snapshot: {snapshot_id} does not exist.",
        )

    if not download:
        return JSONResponse(content=snapshot_data)

    file = snapshot_drive.get(f"{snapshot_data['world_id']}/{snapshot_data['name']}")

    if not file:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return StreamingResponse(file.iter_chunks(4096), media_type="application/zip")


@router.delete("/{snapshot_id}")
async def delete_snapshot(snapshot_id: str):
    snapshot = snapshot_db.get(snapshot_id)

    if not snapshot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Snapshot: {snapshot_id} does not exist.",
        )

    world = worlds_db.get(snapshot["world_id"])

    if not world:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"world: {snapshot['world_id']} does not exist.",
        )

    try:
        snapshot_drive.delete(snapshot["name"])
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    snapshot_db.delete(snapshot_id)

    try:
        worlds_db.update({"num_snapshots": world["num_snapshots"] - 1}, world["key"])
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(
        status_code=200, content=f"Snapshot: {snapshot_id} deleted successfully."
    )


@router.get("/info/")
async def get_snapshots_info():
    results = snapshot_db.fetch()

    all_count = results.count
    all_snapshots = results.items

    while results.last:
        results = snapshot_db.fetch(last=results.last)
        all_count += results.count
        all_snapshots += results.items

    size_of_items = 0

    for snapshot in all_snapshots:
        size_of_items += snapshot["size"]

    return {"count": all_count, "total_size": size_of_items}
