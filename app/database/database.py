from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import settings


engine = create_async_engine(settings.postgres_url)
sessionmaker = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db():
    async with sessionmaker() as session:
        yield session
