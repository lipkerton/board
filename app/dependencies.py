from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db


session = Annotated[AsyncSession, Depends(get_db)]