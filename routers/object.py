from typing import List

from fastapi import APIRouter
from schemas import Object


router = APIRouter()


@router.get('/', response_model=List[Object])
def get_objects():
    return List[Object]


@router.get('/{id}', response_model=Object)
def get_object(id: str):
    return Object


@router.post('/{title}', response_model=Object)
def create_object(title: str):
    return Object


@router.delete('/{id}')
def delete_object(id: str):
    return
