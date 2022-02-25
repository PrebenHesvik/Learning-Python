from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:5325Bergen@localhost/fastapi'
database_name = settings.database_name
username = settings.database_username
password = settings.database_password
port = settings.database_port
hostname = settings.database_hostname

SQLALCHEMY_DATABASE_URL = f'postgresql://{username}:{password}@{hostname}/{database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
