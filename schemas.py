import datetime

from typing import List

from pydantic import BaseModel, Field
from datetime import date


class User(BaseModel):
    id: str
    name: str
    date: datetime.datetime
    admin: bool


class File(BaseModel):
    id: str
    type: str = Field(description="image/model")
    url: str
    zoom: int
    date: datetime.datetime


class Object(BaseModel):
    id: str
    title: str
    date: datetime.datetime
    department_id: str
    description: str = None
    files: List[File]


class Department(BaseModel):
    id: str
    title: str
    date: datetime.datetime
