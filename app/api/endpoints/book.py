from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.book import Book
from app.schemas.book import Book as BookPD
from app.settings.db import get_async_session

router = APIRouter()


@router.get("/{book_id}", response_model=BookPD)
async def get(book_id: int, session: AsyncSession = Depends(get_async_session)) -> BookPD:
    book = await CRUDBase(Book).get(book_id, session)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.get("/", response_model=list[BookPD])
async def get_all(session: AsyncSession = Depends(get_async_session)) -> list[BookPD]:
    books = await CRUDBase(Book).get_all(session)
    if books is None:
        raise HTTPException(status_code=404, detail="Books not found")
    return books


@router.post("/", response_model=BookPD, response_model_exclude_none=True)
async def create(book: BookPD, session: AsyncSession = Depends(get_async_session)):
    return await CRUDBase(Book).create(book, session)


@router.patch("/{book_id}", response_model=BookPD)
async def update(book_id: int, obj_in: BookPD, session: AsyncSession = Depends(get_async_session)):
    book = CRUDBase(Book)
    book_obj = await book.get(book_id, session)
    if book_obj is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return await book.update(book_obj, obj_in, session)


@router.delete("/{book_id}", response_model=BookPD)
async def delete(
    book_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> BookPD:

    book = CRUDBase(Book)
    book_obj = await book.get(book_id, session)
    if book_obj is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return await book.remove(book_obj, session)
