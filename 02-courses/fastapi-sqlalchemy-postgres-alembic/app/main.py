from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine, Base
from .routers import post, user, auth, vote
from .config import settings

### Create tables within postgres ###
# We have imported Base from file database into file models
# and it seems that this is the Base we need to use (maybe)
# BUT we DON'T need this one if we use alembic.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Info on middleware:
# https://fastapi.tiangolo.com/tutorial/middleware/

# CORS (Cross Origin Resource Sharing) IMPORTNT!!!
# https://fastapi.tiangolo.com/tutorial/cors/

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}
