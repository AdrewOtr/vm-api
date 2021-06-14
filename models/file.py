from sqlalchemy import Column, Integer, String, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from models.database import Base


class File(Base):
    __tablename__ = 'file'
    __mapper_args__ = dict(polymorphic_identity="file")

    id = Column(UUID, primary_key=True)
    type = Column(String, default="image")
    url = Column(String)
    zoom = Column(Integer)
    object_id = Column(UUID, ForeignKey('object.id'))
    date = Column(TIMESTAMP, nullable=True, server_default=func.now())
