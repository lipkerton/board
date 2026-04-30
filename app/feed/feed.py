from fastapi import APIRouter


route = APIRouter()

@route.get("/")
def index():
    return {"message": "Hello world!"}

