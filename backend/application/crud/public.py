from application.utils.connections import (
    worlds_db,
    snapshot_db,
    snapshot_drive,
)
from fastapi import HTTPException, status
from fastapi.responses import Response


def grab_shared_world(world_id: str):
    world = worlds_db.get(world_id)

    if not world or world["is_public"] is False:  # type: ignore
        raise HTTPException(
            status_code=404,
            detail={"message": f"World: {world_id} does not exist publicly."},
        )

    latest_snap = snapshot_db.get(world["newest_snapshot"])  # type: ignore

    del world["newest_snapshot"]  # type: ignore
    world["full_size"] = world["size"]  # type: ignore
    del world["size"]  # type: ignore

    del latest_snap["key"]  # type: ignore
    del latest_snap["name"]  # type: ignore
    del latest_snap["world_id"]  # type: ignore

    data = {
        **world,  # type: ignore
        **latest_snap,  # type: ignore
    }

    return data


def download_shared_world(world_id: str, part: int):
    world = worlds_db.get(world_id)

    if not world:
        raise HTTPException(status_code=404)

    snapshot = snapshot_db.get(world["newest_snapshot"])  # type: ignore

    snapshot_id = snapshot["key"]  # type: ignore

    if not snapshot:
        raise HTTPException(
            status_code=404,
            detail={"message": "Snapshot does not exist."},
        )

    try:
        file = snapshot_drive.get(
            f"{snapshot_id}/{snapshot['name']}.part{part}"  # type: ignore
        )
    except Exception:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

    if not file:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

    return Response(file.read(), media_type="application/zip")
