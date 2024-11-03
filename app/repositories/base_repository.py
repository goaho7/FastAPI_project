from abc import ABC, abstractmethod

from sqlalchemy import delete, insert, select, update

from app.settings.db import async_session_maker


class AbstractRepository(ABC):

    @abstractmethod
    async def get(self, obj_id):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError

    @abstractmethod
    async def create(self, data):
        raise NotImplementedError

    @abstractmethod
    async def update(self, data, obj_id):
        raise NotImplementedError

    @abstractmethod
    async def remove(self, obj_id):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def get(self, obj_id: int):
        async with async_session_maker() as session:
            db_obj = await session.execute(select(self.model).where(self.model.id == obj_id))
            return db_obj.scalars().first()

    async def get_all(self):
        async with async_session_maker() as session:
            res = await session.execute(select(self.model))
            return res.scalars().all()

    async def create(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar()

    async def update(self, data: dict, obj_id: int):
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.id == obj_id).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar()

    async def remove(self, obj_id: int):
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.id == obj_id)
            res = await session.execute(stmt)
            await session.commit()
            return res
