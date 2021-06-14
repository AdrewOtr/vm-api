from typing import List

from fastapi import APIRouter, Depends, HTTPException
import models
import schemas
from models.database import Session

router = APIRouter()


@router.get('/', response_model=schemas.ObjectList[schemas.Object])
def get_objects():
    session = Session()
    objects_out = session.query(models.Object).all()
    obj_list = schemas.ObjectList(objects=objects_out)
    return obj_list


@router.get('/{id}', response_model=schemas.Object)
def get_object(id: str):
    session = Session()
    object_out = session.query(models.Object).filter(models.Object.id == id).first()
    return object_out


@router.post('/{title}', response_model=schemas.Object)
def create_object(title: str):
    return


@router.delete('/{id}')
def delete_object(id: str):
    return
