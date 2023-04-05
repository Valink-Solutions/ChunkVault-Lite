from application.crud.actions import delete_snapshots
from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter()


class Event(BaseModel):
    id: str
    trigger: str


@router.post("/")
async def action(event: Event = Body(...)):
    parsed_event = event.dict()

    if parsed_event.get("id") == "cleanup":
        delete_snapshots()
