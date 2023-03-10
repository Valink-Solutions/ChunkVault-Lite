from pydantic import BaseModel


class NewSnapshotSchema(BaseModel):
    world_id: str
    size: int
