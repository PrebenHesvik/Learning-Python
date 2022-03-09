from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(prefix='/users', tags=['Users'])


class CommitData():

    def __init__(self, db, data):
        self.db = db
        self.data = data

    def __enter__(self):
        self.db.add(self.data)

    def __exit__(self, exc_type, exc_val, traceback):
        self.db.commit()
        self.db.refresh(self.data)


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hash the password
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    with CommitData(db, new_user):
        return new_user


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserOut)
def create_user_old(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hash the password
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    print('get user is running')
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id of "{id}" does not exist'
        )
    return user
