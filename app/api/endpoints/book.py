from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.depensens import book_service
from app.schemas.book import BookSchema, BookUpdateSchema
from app.services.book import BookService

router = APIRouter()


@router.get("/{book_id}", status_code=status.HTTP_200_OK)
async def get(book_id: int, service: Annotated[BookService, Depends(book_service)]) -> BookSchema:
    return await service.get(book_id)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all(service: Annotated[BookService, Depends(book_service)]) -> list[BookSchema]:
    return await service.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(book: BookSchema, service: Annotated[BookService, Depends(book_service)]):
    return await service.create(book)


@router.patch("/{book_id}", response_model=BookSchema, status_code=status.HTTP_200_OK)
async def update(book_id: int, data: BookUpdateSchema, service: Annotated[BookService, Depends(book_service)]):
    return await service.update(data, book_id)


@router.delete("/{book_id}")
async def delete(book_id: int, service: Annotated[BookService, Depends(book_service)]):
    return await service.remove(book_id)
