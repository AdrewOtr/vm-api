from typing import List

from fastapi import APIRouter
from schemas import Department, Object


router = APIRouter()


@router.get('/', response_model=List[Department])
def get_departments():
    return


@router.get('/{id}', response_model=Department)
def get_department(id: str):
    return


@router.get('/{id}/objects', response_model=List[Object])
def get_department_objects(id: str):
    return


@router.post('/{title}', response_model=Department)
def create_department(title: str):
    return


@router.delete('/{id}')
def delete_department(id: str):
    return
