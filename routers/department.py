from typing import List

from fastapi import APIRouter
from schemas import Department


router = APIRouter()


@router.get('/', response_model=List[Department])
def get_departments():
    return List[Department]


@router.get('/{id}', response_model=Department)
def get_department(id: str):
    return Department


@router.post('/{title}', response_model=Department)
def create_department(title: str):
    return Department


@router.delete('/{id}')
def delete_department(id: str):
    return
