from fastapi import APIRouter
from . import schemas


route = APIRouter()

@route.get("/")
def feed():
    return {"message": "Hello world!"}


@route.post("/post")
def post(post: schemas.Post):
    return post
