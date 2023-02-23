from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse

from application.utils.databases import worlds_db, snapshot_db
from application.schemas.worlds import NewWorldSchema, WorldSchema, UpdateWorldSchema
from application.utils import remove_none_values

router = APIRouter()
    
    
@router.get("/")
async def get_worlds(last: str = None, limit: int = 100):
    
    results = worlds_db.fetch(limit=limit, last=last)
    
    if not results.count > 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No worlds found.")
    
    return {
        "count": results.count,
        "last": results.last,
        "items": results.items        
    }


@router.post("/")
async def create_new_world(data: NewWorldSchema = Body(...)):

    new_world = WorldSchema(**data.dict())
    
    results = worlds_db.fetch({"name": new_world.name})
    
    if results.count > 0:
        return HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED, detail=f"World: {new_world.name} already exists.")
    
    result = worlds_db.put(new_world.dict())
    
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
    return JSONResponse(content={
        "world_id": result["key"],
    })
    
@router.patch("/{world_id}")
async def update_world(world_id: str, data: UpdateWorldSchema = Body(...)):
    
    world = worlds_db.get(world_id)
    
    if not world:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"World: {world_id} does not exist.")
    
    parsed_data = remove_none_values(data.dict())
    
    try:
        worlds_db.update(parsed_data, world["key"])
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"World: {world_id} could not be updated.")
    
    return JSONResponse(status_code=200, content=f"World: {world_id} was updated.")
    
@router.get("/{world_id}")
async def get_world(world_id: str):
    world = worlds_db.get(world_id)
    
    if not world:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"World: {world_id} does not exist.")
    
    results = snapshot_db.fetch({"world_id": world_id})
    
    return JSONResponse(content={
        **world,
        "snapshots": results.items
    })
    
    
@router.get("/find/{world_name}")
async def find_world(world_name: str):
    
    results = worlds_db.fetch({"name": world_name})
    
    if not results.count > 0:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"World: {world_name} does not exist.")
    
    world = results.items[0]
    
    return world