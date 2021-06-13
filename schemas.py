from typing import Optional, List

from pydantic import BaseModel, Field


class User(BaseModel):
    id: str
    name: str
    date: str
    admin: bool


class File(BaseModel):
    id: str
    type: str = Field(description="image/model")
    url: str
    zoom: int
    date: str


class Object(BaseModel):
    id: str
    title: str
    date: str
    department_id: str
    description: Optional[str] = None
    # files: List[File]


class Department(BaseModel):
    id: str
    title: str
    date: str
