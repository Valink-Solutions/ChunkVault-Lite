import time
from typing import Union
from application.utils.connections import (
    upload_session_db,
    worlds_db,
    snapshot_db,
    shard_drive,
)

from fastapi import BackgroundTasks, UploadFile, File, HTTPException, status
from fastapi.responses import JSONResponse, Response, StreamingResponse


def create_snapshot(world_id: str, size: int):
    world = worlds_db.get(world_id)

    if not world:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"World: {world_id} does not exist."},
        )

    current_time = int(time.time())

    try:
        snapshot = snapshot_db.put(
            {
                "world_id": world_id,
                "name": f"{current_time}-snapshot",
                "parts": 0,
                "size": size,
                "created_at": current_time,
            }
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return snapshot


async def delete_parts(part_range, snapshot_id, snapshot_name):
    for part in part_range:
        try:
            shard_drive.delete(
                f"{snapshot_id}/{snapshot_name}.part{part+1}"  # type: ignore
            )
        except Exception:
            continue


async def delete_snapshot(snapshot_id: str, background_tasks: BackgroundTasks):
    snapshot = snapshot_db.get(snapshot_id)

    if not snapshot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"Snapshot: {snapshot_id} does not exist."},
        )

    parts = snapshot["parts"]  # type: ignore

    snapshot_name = snapshot["name"]  # type: ignore

    if parts > 50:
        chunk_size = 10
        part_chunks = [
            range(i, i + chunk_size) for i in range(1, parts + 1, chunk_size)
        ]
        for chunk in part_chunks:
            background_tasks.add_task(delete_parts, chunk, snapshot_id, snapshot_name)
    else:
        await delete_parts(range(parts), snapshot_id, snapshot_name)

    world_id = snapshot["world_id"]  # type: ignore

    world = worlds_db.get(world_id)

    if not world:
        raise HTTPException(status_code=500)

    try:
        snapshot_db.delete(snapshot_id)

        worlds_db.update(
            {"num_snapshots": world["num_snapshots"] - 1}, world_id  # type: ignore
        )

    except Exception:
        raise HTTPException(status_code=500)

    return JSONResponse(
        content={"message": f"Snapshot: {snapshot_id} successfully delete."}
    )


def generate_session(snapshot_id: str, name: str):
    snapshot = snapshot_db.get(snapshot_id)

    if not snapshot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"Snapshot: {snapshot_id} does not exist."},
        )

    try:
        session = upload_session_db.put(
            {
                "snapshot_id": snapshot_id,
                "name": name,
                "current_part": 0,
            }
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return session


async def upload_chunk(
    snapshot_id: str,
    session_id: str,
    name: str,
    part: int = 1,
    file: UploadFile = File(...),
):
    session = upload_session_db.get(session_id)

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Session: {session_id} does not exist.",
        )

    if not session["name"] == name:  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Session: {name} does not match file name.",
        )

    if not session["current_part"] < part:  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_208_ALREADY_REPORTED,
            detail=f"Session: {part} already written.",
        )

    snapshot = snapshot_db.get(snapshot_id)

    if not snapshot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Snapshot: {snapshot_id} does not exist.",
        )

    if not snapshot_id == snapshot["key"]:  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Snapshot: {snapshot_id} does not match session.",
        )

    try:
        await file.seek(0)

        shard_drive.put(
            f"{snapshot['key']}/{snapshot['name']}.part{part}",  # type: ignore
            await file.read(),
        )

        upload_session_db.update(
            {
                "current_part": session["current_part"] + 1,  # type: ignore
            },
            session_id,
        )  # type: ignore
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error uploading part: {part}",
        )

    return JSONResponse(content={"message": f"Sucessfully uploaded part: {part}"})


def finish_session(session_id: str, name: str):
    session = upload_session_db.get(session_id)

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Session: {session_id} does not exist.",
        )

    if not session["name"] == name:  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Session: {name} does not match file name.",
        )

    snapshot = snapshot_db.get(session["snapshot_id"])  # type: ignore

    snapshot_id = session["snapshot_id"]  # type: ignore

    if not snapshot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Snapshot: {snapshot_id} does not exist.",
        )

    try:
        snapshot_db.update(
            {
                "parts": session["current_part"],  # type: ignore
            },
            session["snapshot_id"],  # type: ignore
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    upload_session_db.delete(session_id)

    world = worlds_db.get(snapshot["world_id"])  # type: ignore

    if not world:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    try:
        worlds_db.update(
            {
                "num_snapshots": world["num_snapshots"] + 1,  # type: ignore
                "newest_snapshot": snapshot_id,
            },
            snapshot["world_id"],  # type: ignore
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return snapshot


def abort_session(session_id: str, name: str):
    session = upload_session_db.get(session_id)

    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"Session: {session_id} does not exist."},
        )

    if not session["name"] == name:  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": f"Session: {name} does not match file name."},
        )

    snapshot = snapshot_db.get(session["snapshot_id"])  # type: ignore

    if not snapshot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    for part in range(session["current_part"]):  # type: ignore
        try:
            shard_drive.delete(
                f"{snapshot['key']}/{snapshot['name']}.part{part+1}"  # type: ignore
            )
        except Exception as e:
            print(e)
            continue
    try:
        snapshot_db.delete(session["snapshot_id"])  # type: ignore
    except Exception as e:
        print(e)

    try:
        upload_session_db.delete(session_id)
    except Exception as e:
        print(e)

    return JSONResponse(
        content={"message": f"Session: {session_id} deleted successfully."}
    )


def download_snapshot_part(snapshot_id: str, part: int = 1):
    snapshot = snapshot_db.get(snapshot_id)

    if not snapshot:
        raise HTTPException(
            status_code=404,
            detail={"message": f"Snapshot: {snapshot_id} does not exist."},
        )

    try:
        file = shard_drive.get(
            f"{snapshot_id}/{snapshot['name']}.part{part}"  # type: ignore
        )
    except Exception:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

    if not file:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

    return Response(file.read(), media_type="application/zip")


def download_full_snapshot(snapshot_id: str):
    snapshot = snapshot_db.get(snapshot_id)

    if not snapshot:
        raise HTTPException(
            status_code=404,
            detail={"message": f"Snapshot: {snapshot_id} does not exist."},
        )

    world = worlds_db.get(snapshot["world_id"])  # type: ignore

    if not world:
        raise HTTPException(status_code=500)

    parts = snapshot["parts"]  # type: ignore

    def get_parts():
        for part in range(parts):
            file = shard_drive.get(
                f"{snapshot_id}/{snapshot['name']}.part{part+1}"  # type: ignore
            )

            if not file:
                raise Exception

            yield file.read()

    file_name = f"{world['name']}.zip"  # type: ignore

    return StreamingResponse(
        get_parts(),
        media_type="application/zip",
        headers={"Content-Disposition": f'attachment; filename="{file_name}"'},
    )


def grab_snapshot(snapshot_id: str):
    snapshot = snapshot_db.get(snapshot_id)

    if not snapshot:
        raise HTTPException(
            status_code=404,
            detail={"message": f"Snapshot: {snapshot_id} does not exist."},
        )

    return snapshot


def grab_snapshots(last: Union[str, None] = None, limit: int = 100):
    results = snapshot_db.fetch(last=last, limit=limit)  # type: ignore

    if not results.count > 0:
        raise HTTPException(status_code=404, detail={"message": "No snapshots found."})

    return JSONResponse(
        content={"count": results.count, "last": results.last, "items": results.items}
    )


def snapshot_size_on_disk():
    results = snapshot_db.fetch()

    final_count = results.count
    final_items = results.items

    while results.last:
        results = snapshot_db.fetch(last=results.last)
        final_items += results.items

    full_size = 0.0

    for snapshot in final_items:
        full_size += snapshot.get("size")

    return JSONResponse(content={"num_snapshots": final_count, "size": full_size})
