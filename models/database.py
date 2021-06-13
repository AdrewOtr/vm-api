from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


sqlalchemy_database_url = f"postgresql://postgres:123@localhost:5432/vm_test"

engine = create_engine(sqlalchemy_database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)
