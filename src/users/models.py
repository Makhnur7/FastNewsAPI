"""
<<<<<<< HEAD
FastAPI users
"""
from datetime import datetime
from typing import AsyncGenerator


from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTableUUID
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from src.database import session as async_session, Base

=======
User model
"""

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Base, get_db
>>>>>>> 2cb9f00 (Authorization and registration for users)


class User(SQLAlchemyBaseUserTableUUID, Base):
    """
<<<<<<< HEAD
    User model
    """    
    full_name: Mapped[str] = mapped_column(nullable=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)



=======
    User model with UUID id column
    """

    __tablename__ = "user"

    full_name: Mapped[str] = mapped_column(String(length=100), nullable=False)


async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)
>>>>>>> 2cb9f00 (Authorization and registration for users)
