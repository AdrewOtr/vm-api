from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.database import Base


class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(String)
    object = relationship('Object')

    # def __repr__(self):
    #     return f'Группа [ID: {self.id}, Название: {self.group_name}]'
