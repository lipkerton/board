from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import settings
from app.feed import feed


app = FastAPI()


app.include_router(feed.route)
app.mount("/static", StaticFiles(directory=settings.STATIC_DIR))
