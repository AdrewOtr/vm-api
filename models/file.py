from sqlalchemy import Column, Integer, String, ForeignKey

from models.database import Base


class File(Base):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    url = Column(String)
    zoom = Column(Integer)
    object_id = Column(Integer, ForeignKey('object.id'))
