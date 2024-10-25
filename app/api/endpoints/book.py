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
