from typing import List

from pydantic import BaseModel
from datetime import date


class Entity(BaseModel):
    id: str
    name: str
    date: date


class User(Entity):
    admin: bool
    entity: Entity


class File(BaseModel):
    url: str
    zoom: int


class Object(Entity):
    type: str   # image/model
    description: str
    files: List[File]


