from models.database import Session
from models.department import Department
from models.object import Object
from models.file import File

import uuid
from os import listdir


def create_database(load_data: bool = True):
    if load_data:
        create_data(Session())


def create_data(session: Session):
    department1_id = uuid.uuid4().hex
    department2_id = uuid.uuid4().hex
    department1 = Department(id=department1_id, title='Биология и Общая генетика')
    department2 = Department(id=department2_id, title='Биотехнология')
    session.add(department1)
    session.add(department2)

    mypath = "C:/Users/Andrey/Pictures/PNG"
    onlyfiles = listdir(mypath)
    added_objects = []

    for obj in onlyfiles:
        splited_obj = obj.split('_')
        if splited_obj[0] in added_objects:
            continue
        obj_id = uuid.uuid4().hex
        new_object = Object(id=obj_id, title=splited_obj[0], department_id=department1_id)
        session.add(new_object)
        for fl in onlyfiles:
            splited_fl = fl.split('_')
            zoom_fl = splited_fl[1].split('.')
            if fl.find(splited_obj[0]) != -1:
                fl_id = uuid.uuid4().hex
                new_file = File(id=fl_id, type='image', url=fl, zoom=zoom_fl[0], object_id=obj_id)
                session.add(new_file)
        added_objects.append(splited_obj[0])

    session.commit()
    session.close()
