"""This code is only to show how to use psycopg2 library instead of sqlalchemy"""
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


try:
    conn = psycopg2.connect(
        host='localhost',
        database='fastapi',
        user='postgres',
        password='password',
        # The main advantage of real dictionary cursor is the easiness to get a query output as json.
        # link for more info: https://stackoverflow.com/questions/45399347/psycopg2-dictcursor-vs-realdictcursor
        cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print('Database connection was successfull. ')

except Exception as error:
    print('Connection to database failed')
    print(error)


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {'data': posts}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(
        """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
        vars=(post.title, post.content, post.published)
    )
    new_post = cursor.fetchone()
    # We always have to commit when we create new data
    conn.commit()
    return {'data': new_post}


@app.get('/posts/{id}')
def get_post(id: int):
    cursor.execute("""SELECT * from posts WHERE id = %s""", vars=(str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Post with id of "{id}" was not found'
        )
    return post


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(
        """DELETE FROM posts WHERE id = %s returning *""", vars=(str(id))
    )
    deleted_post = cursor.fetchone()
    if deleted_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Post with id of "{id}" was not found'
        )
    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    cursor.execute(
        """
        UPDATE posts SET title = %s, content = %s,
        published = %s WHERE id = %s RETURNING *
        """,
        vars=(post.title, post.content, post.published, str(id))
    )
    updated_post = cursor.fetchone()
    print(updated_post)
    conn.commit()

    if updated_post is None:
        print('ERROR')
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Post with id of "{id}" was not found'
        )
    return {'data': updated_post}
