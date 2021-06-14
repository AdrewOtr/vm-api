import datetime
from typing import Optional, List, Generic, TypeVar

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

import stringcase

DataT = TypeVar('DataT')
RefSchemaType = TypeVar("RefSchemaType", bound=BaseModel)


def to_camel(string):
    return stringcase.camelcase(string)


# Use this model as the base for entity base models instead of entity base to eliminate circular imports
class CamelCaseModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class User(BaseModel):
    id: Optional[str]
    name: Optional[str]
    date: Optional[datetime.datetime]
    admin: Optional[bool]

    class Config:
        orm_mode = True


class File(BaseModel):
    id: Optional[str]
    type: Optional[str] = Field(description="image/model")
    url: Optional[str]
    zoom: Optional[int]
    date: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class FileList(GenericModel, CamelCaseModel, Generic[RefSchemaType]):
    files: List[File] = []

    class Config:
        orm_mode = True


class Object(BaseModel):
    id: Optional[str]
    title: Optional[str]
    date: Optional[datetime.datetime]
    department_id: Optional[str]
    description: Optional[str] = None
    files: Optional[FileList[File]] = None

    class Config:
        orm_mode = True


class ObjectList(GenericModel, CamelCaseModel, Generic[RefSchemaType]):
    objects: List[Object] = []

    class Config:
        orm_mode = True


class Department(BaseModel):
    id: Optional[str]
    title: Optional[str]
    date: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class DepartmentList(GenericModel, CamelCaseModel, Generic[RefSchemaType]):
    departments: List[Department] = []

    class Config:
        orm_mode = True


# # Generic response wrapper
# class Payload(GenericModel, Generic[DataT]):
#     data: Optional[DataT]
#
#     class Config:
#         orm_mode = True
