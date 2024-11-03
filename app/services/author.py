from fastapi import HTTPException

from app.repositories.base_repository import AbstractRepository
from app.schemas.author import AuthorSchema, AuthorUpdateSchema


class AuthorService:
    def __init__(self, author_repository: AbstractRepository, tag_repository: AbstractRepository):
        self.author_repository: AbstractRepository = author_repository()
        self.tag_repository: AbstractRepository = tag_repository()

    async def get(self, obj_id: int):
        obj = await self.author_repository.get(obj_id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Author not found")
        return obj

    async def get_all(self):
        return await self.author_repository.get_all()

    async def create(self, data: AuthorSchema):
        data_dict = data.model_dump()
        tags = data_dict.pop("tags")
        missing_tags = await self.missing_tags(tags)
        if missing_tags:
            raise HTTPException(status_code=404, detail=f"Tags with id {missing_tags} not found.")
        author = await self.author_repository.create(data_dict)
        if tags:
            await self.tag_repository.add_tags_to_author(author.id, tags)
        return author

    async def update(self, data: AuthorUpdateSchema, obj_id: int):
        data_dict = data.model_dump(exclude_unset=True)
        obj = await self.author_repository.update(data_dict, obj_id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Author not found")
        return obj

    async def remove(self, obj_id: int):
        res = await self.author_repository.remove(obj_id)
        if res.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Author with id {obj_id} not found.")
        return {"message": "The object has been removed."}

    async def missing_tags(self, tags: list | None):
        missing_tags = []
        if tags:
            for tag_id in tags:
                tag = await self.tag_repository.get(tag_id)
                if tag is None:
                    missing_tags.append(tag_id)
        return missing_tags
