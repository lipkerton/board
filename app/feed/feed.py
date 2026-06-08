from sqlalchemy import select
from sqlalchemy.orm import load_only
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config import settings
from app.dependencies import session
from app.database.models import Post
from . import schemas


route = APIRouter()

templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)


@route.get("/", response_class=HTMLResponse)
async def feed(session: session, request: Request):
    query = (
        select(Post)
        .order_by(Post.created_at.desc())
    )
    result = await session.execute(query)
    posts = result.all()

    
    return templates.TemplateResponse(
        request=request, name="feed.html", context={"posts": []}
    )


@route.post("/post")
def post(post: schemas.Post):
    return post
