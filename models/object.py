from sqlalchemy import Column, func, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from models.database import Base


class Object(Base):
    __tablename__ = 'object'

    id = Column(UUID, primary_key=True)
    title = Column(String)
    date = Column(TIMESTAMP, nullable=True, server_default=func.now())
    department_id = Column(UUID, ForeignKey('department.id'))
    description = Column(String)
    file = relationship('File')
