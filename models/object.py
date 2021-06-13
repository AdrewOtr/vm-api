from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Object(Base):
    __tablename__ = 'object'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(String)
    department_it = Column(Integer, ForeignKey('department.id'))
    description = Column(String)
    object = relationship('File')

    def __init__(self, title: str, date: str, department_it: str, description: str):
        self.title = title
        self.date = date
        self.department_it = department_it
        self.description = description

    # def __repr__(self):
    #     info: str = f'Студент [ФИО: {self.surname} {self.name} {self.patronymic}, ' \
    #         f'Возраст: {self.age}, Адрес: {self.address}, ID группы: {self.group}]'
    #     return info
