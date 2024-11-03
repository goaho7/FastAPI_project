from fastapi import HTTPException

from app.repositories.base_repository import AbstractRepository
from app.schemas.tag import TagSchema, TagUpdateSchema


class TagService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository()

    async def get(self, obj_id: int):
        obj = await self.repository.get(obj_id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Tag not found")
        return obj

    async def get_all(self):
        return await self.repository.get_all()

    async def create(self, data: TagSchema):
        data_dict = data.model_dump()
        obj = await self.repository.create(data_dict)
        return obj

    async def update(self, data: TagUpdateSchema, obj_id: int):
        data_dict = data.model_dump(exclude_unset=True)
        obj = await self.repository.update(data_dict, obj_id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Tag not found")
        return obj

    async def remove(self, obj_id: int):
        res = await self.repository.remove(obj_id)
        if res.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Tag with id {obj_id} not found.")
        return {"message": "The object has been removed."}
