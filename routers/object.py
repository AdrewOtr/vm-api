from typing import List

from fastapi import APIRouter, Depends, HTTPException
from schemas import Object
from models.database import Session

router = APIRouter()


@router.get('/', response_model=List[Object])
def get_objects():
    return


@router.get('/{id}', response_model=Object)
def get_object(id: str):
    session = Session()
    object_out = session.query(Object).filter(Object.id == id)
    return object_out


@router.post('/{title}', response_model=Object)
def create_object(title: str):
    return


@router.delete('/{id}')
def delete_object(id: str):
    return
