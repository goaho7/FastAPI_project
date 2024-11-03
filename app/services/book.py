from fastapi import (
    HTTPException,
)

from app.repositories.base_repository import (
    AbstractRepository,
)
from app.schemas.book import (
    BookSchema,
    BookUpdateSchema,
)


class BookService:
    def __init__(
        self,
        book_repository: AbstractRepository,
        author_repository: AbstractRepository,
    ):
        self.book_repository: AbstractRepository = book_repository()
        self.author_repository: AbstractRepository = author_repository()

    async def get(self, obj_id: int):
        obj = await self.book_repository.get(obj_id)
        if obj is None:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )
        return obj

    async def get_all(self):
        return await self.book_repository.get_all()

    async def create(self, data: BookSchema):
        data_dict = data.model_dump()
        author_id = data_dict["author_id"]
        author = await self.author_repository.get(author_id)
        if author is None:
            raise HTTPException(
                status_code=404,
                detail=f"Author with id {author_id} not found.",
            )
        return await self.book_repository.create(data_dict)

    async def update(
        self,
        data: BookUpdateSchema,
        obj_id: int,
    ):
        data_dict = data.model_dump(exclude_unset=True)
        author_id = data_dict.get("author_id")
        if author_id:
            author = await self.author_repository.get(author_id)
            if author is None:
                raise HTTPException(
                    status_code=404,
                    detail=f"Author with id {author_id} not found.",
                )
        obj = await self.book_repository.update(data_dict, obj_id)
        if obj is None:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )
        return obj

    async def remove(self, obj_id: int):
        res = await self.book_repository.remove(obj_id)
        if res.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail=f"Book with id {obj_id} not found.",
            )
        return {"message": "The object has been removed."}
