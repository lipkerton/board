from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config import settings
from . import schemas


route = APIRouter()

templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)


@route.get("/", response_class=HTMLResponse)
async def feed(request: Request):
    return templates.TemplateResponse(
        request=request, name="feed.html", context={"posts": []}
    )


@route.post("/post")
def post(post: schemas.Post):
    return post
