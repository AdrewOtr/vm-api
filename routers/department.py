from typing import List
from models import Department, Object
from fastapi import APIRouter
import schemas
from models.database import Session


router = APIRouter()


@router.get('/', response_model=schemas.DepartmentList[schemas.Department])
def get_departments():
    session = Session()
    dep_out = session.query(Department).all()
    dep_list = schemas.DepartmentList(departments=dep_out)
    return dep_list


@router.get('/{id}', response_model=schemas.Department)
def get_department(id: str):
    session = Session()
    dep_out = session.query(Department).filter(Department.id == id).first()
    return dep_out


@router.get('/{id}/objects', response_model=schemas.ObjectList[schemas.Object])
def get_department_objects(id: str):
    session = Session()
    obj_out = session.query(Object).join(Department).filter(Department.id == id).all()
    obj_list = schemas.ObjectList(objects=obj_out)
    return obj_list


@router.post('/{title}', response_model=schemas.Department)
def create_department(title: str):
    return


@router.delete('/{id}')
def delete_department(id: str):
    return
