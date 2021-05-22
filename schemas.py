from typing import List

from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    id: str
    name: str
    date: date
    admin: bool


class File(BaseModel):
    url: str
    zoom: int


class Object(BaseModel):
    type: str   # image/model
    description: str
    files: List[File]
    id: str
    name: str
    date: date


class Department(BaseModel):
    id: str
    name: str
    date: date

