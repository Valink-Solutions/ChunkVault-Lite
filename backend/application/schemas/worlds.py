from typing import Union
from pydantic import BaseModel


class NewWorldSchema(BaseModel):
    name: str
    size: int
    is_public: Union[bool, None] = False


class WorldSchema(BaseModel):
    name: str
    size: int
    is_public: bool
    image: Union[str, None] = None
    num_snapshots: Union[int, None] = 0


class UpdateWorldSchema(BaseModel):
    name: Union[str, None] = None
    size: Union[int, None] = None
    is_public: Union[bool, None] = None
    image: Union[str, None] = None
