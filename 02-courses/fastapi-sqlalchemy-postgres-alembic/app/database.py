from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# The Object Relational Mapper (ORM) is a layer of abstraction that sits between the database and fastapi
# and allows us to perform all database operations through traditional python code.
# SQLAlchemy uses psycopg2 to talk to the database so it is important that this driver is also installed.

# Through the classes in models.py we create the tables that we want in our database,
# so we don't have to create the tables using sql or PgAdmin.

# Some documentation: https://fastapi.tiangolo.com/tutorial/sql-databases/

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
database_name = settings.database_name
username = settings.database_username
password = settings.database_password
port = settings.database_port
hostname = settings.database_hostname

SQLALCHEMY_DATABASE_URL = f'postgresql://{username}:{password}@{hostname}/{database_name}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal is used in the get_db function below
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is imported in models.py and is the parent class of the models we create there
Base = declarative_base()

## QLALCHEMY_DATABASE_URL ###
# If we were to use sqlite:
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

### SessionLocal ###
# Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.
# But once we create an instance of the SessionLocal class, this instance will be the actual database session.
# We name it SessionLocal to distinguish it from the Session we are importing from SQLAlchemy.

### declarative_base() ###
# declarative_base() returns a class


def get_db():
    """
    Dependency
    Imported by the router files
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
