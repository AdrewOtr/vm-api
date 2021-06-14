from fastapi import APIRouter, Depends, HTTPException
from models import Object, File
import schemas
from models.database import Session

router = APIRouter()


@router.get('/', response_model=schemas.ObjectList[schemas.Object])
def get_objects():
    session = Session()
    objects_out = session.query(Object).all()
    obj_list = schemas.ObjectList(objects=objects_out)
    return obj_list


@router.get('/{id}', response_model=schemas.Object)
def get_object(id: str):
    session = Session()
    object_out = session.query(Object).filter(Object.id == id).first()
    return object_out


@router.get('/{id}/files', response_model=schemas.FileList[schemas.File])
def get_object_files(id: str):
    session = Session()
    files_out = session.query(File).join(Object).filter(Object.id == id).all()
    file_list = schemas.FileList(files=files_out)
    return file_list


@router.post('/{title}', response_model=schemas.Object)
def create_object(title: str):
    return


@router.delete('/{id}')
def delete_object(id: str):
    return
