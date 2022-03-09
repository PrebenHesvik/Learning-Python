from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])

# Link to site with information on OAuthPasswordRequestForm
# https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/


@router.post('/login', response_model=schemas.Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db)
):
    # OAuth2PasswordRequestForm will return a dict
    # {'username': 'this will be the email',
    #  'password': 'this is the password'}
    user = (
        db
        .query(models.User)
        .filter(models.User.email == user_credentials.username)
        .first()
    )
    if user and utils.verify(user_credentials.password, user.password):
        access_token = oauth2.create_access_token(data={'user_id': user.id})
        return {
            'access_token': access_token,
            'token_type': 'bearer'
        }
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Invalid Credentials',
    )


@router.post('/login', response_model=schemas.Token)
def login_old(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db)
):
    # OAuth2PasswordRequestForm will return a dict
    # {'username': 'this will be the email',
    #  'password': 'this is the password'}
    user = (
        db
        .query(models.User)
        .filter(models.User.email == user_credentials.username)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Invalid Credentials',
        )
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Invalid Credentials',
        )
    access_token = oauth2.create_access_token(data={'user_id': user.id})

    return {
        'access_token': access_token,
        'token_type': 'bearer',
    }
