from typing import AsyncGenerator

from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import (
    Mapped,
    declarative_base,
    declared_attr,
    mapped_column,
    sessionmaker,
)
from sqlalchemy.sql import func

from app.settings.config import settings


class PreBase:

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at = mapped_column(DateTime, default=func.now(), nullable=False, index=True)
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False, index=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=PreBase)


engine = create_async_engine(settings.ASYNC_POSTGRES_CONNECT)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Асинхронный генератор сессий."""
    async with AsyncSessionLocal() as async_session:
        yield async_session
