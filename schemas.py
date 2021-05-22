from typing import List

from pydantic import BaseModel, Field
from datetime import date


class User(BaseModel):
    id: str
    name: str
    date: date
    admin: bool


class File(BaseModel):
    id: str
    url: str
    zoom: int


class Object(BaseModel):
    id: str
    title: str
    date: date
    type: str = Field(description="image/model")
    description: str = None
    files: List[File]


class Department(BaseModel):
    id: str
    title: str
    date: date

