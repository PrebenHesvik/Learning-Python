from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
from .. import models, schemas, oauth2
from ..database import get_db

# router will be imported in main.py and inserted into app.include_router()
router = APIRouter(prefix='/posts', tags=['Posts'])

### prefix ###
# All api paths in this file will start with /posts

### tags ###
# The name the apis in this file will be listed under in the documentation


# The api structure works top to bottom, so be careful when placing
# the different functions. For example, a url with structure
# "posts/latest" at the bottom would not work because python
# would first find "post/id" and intrepret "latest" as the id
# we are looking for.


### Depends ###
# this stands for dependency
# link for more information: https://fastapi.tiangolo.com/tutorial/dependencies/

# Remember to put List[schemas.PostOut] and not just schemas.PostOut
# since we want to return a list of posts
@router.get('/', response_model=List[schemas.PostOut])
def get_posts(
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
    limit: int = 10,
    skip: int = 0,
    search: Optional[str] = '',
):
    return (
        db
        .query(models.Post, func.count(models.Vote.post_id).label('votes'))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.title.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )


@router.post(
    '/',
    # the status code gets returned to the sender of the post request
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.Post)
def create_posts(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    """
    post has the type of pydantic model. All pydantic models have the 
    dict method which returns the fields as a dictionary.
    """
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get('/{id}', response_model=schemas.PostOut)
def get_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    post = (
        db
        .query(models.Post, func.count(models.Vote.post_id).label('votes'))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .first()
    )
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Post with id of "{id}" was not found'
        )
    return post


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
        id: int,
        db: Session = Depends(get_db),
        current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Post with id of "{id}" was not found'
        )
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Not authorized to perform requested action'
        )
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}', response_model=schemas.Post)
def update_post(
    id: int,
    updated_post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    original_post = post_query.first()
    if original_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Post with id of "{id}" was not found'
        )
    if original_post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Not authorized to perform requested action'
        )
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
