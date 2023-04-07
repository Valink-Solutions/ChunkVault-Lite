import time
from typing import Union
from pydantic import BaseModel, Field


class NewWorldSchema(BaseModel):
    name: str
    seed: str
    difficulty: int
    size: int
    is_public: Union[bool, None] = False
    image: Union[str, None] = None


class WorldSchema(BaseModel):
    name: str
    seed: str
    difficulty: int
    size: int
    is_public: bool
    image: Union[str, None] = None
    num_snapshots: Union[int, None] = 0
    created: Union[float, None] = Field(default_factory=time.time)


class UpdateWorldSchema(BaseModel):
    name: Union[str, None] = None
    seed: Union[str, None] = None
    difficulty: Union[int, None] = None
    size: Union[int, None] = None
    is_public: Union[bool, None] = None
    image: Union[str, None] = None
