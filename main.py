from fastapi import FastAPI
from app.feed import feed


app = FastAPI()

app.include_router(feed.route)