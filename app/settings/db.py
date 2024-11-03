from typing import AsyncGenerator

from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.settings.config import settings

BaseModel = declarative_base()


class Base(BaseModel):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at = mapped_column(DateTime, default=func.now(), nullable=False, index=True)
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False, index=True)


engine = create_async_engine(settings.async_postgres_connect)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Асинхронный генератор сессий."""
    async with async_session_maker() as async_session:
        yield async_session
