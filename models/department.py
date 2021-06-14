from sqlalchemy import Column, func, String
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import relationship

from models.database import Base


class Department(Base):
    __tablename__ = 'department'
    __mapper_args__ = dict(polymorphic_identity="department")

    id = Column(UUID, primary_key=True)
    title = Column(String)
    date = Column(TIMESTAMP, nullable=True, server_default=func.now())
    object = relationship('Object')
