from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

"""
    - Schema/pydantic models define the structure of a request & response.
    
    - The request comes from the user and the recipient is fastapi.

    - This ensure that when a user wants to create a post, the request will
      only go through if it has a the correct structure. In this project
      that means that it has both a title and content in the body.
"""


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
    # Pydantic's orm_mode will tell the Pydantic model to read the data
    # even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).
    # Link for more info: https://fastapi.tiangolo.com/tutorial/sql-databases/#use-pydantics-orm_mode


class Post(PostBase):
    """Used by update_post() in post.py and PostOUt class in schemas"""
    id: int
    created_at: datetime
    # we can include the next two because the post table is linked up with the user table
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    """
    Used by post.get_posts() and post.get_post()
    """
    Post: Post
    # we can include votes since we have included the count
    # of votes in both sql queries
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
