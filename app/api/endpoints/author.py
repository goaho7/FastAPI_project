from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.author import Author
from app.schemas.author import Author as AuthorPD
from app.settings.db import get_async_session

router = APIRouter()


@router.get("/{author_id}", response_model=AuthorPD)
async def get(author_id: int, session: AsyncSession = Depends(get_async_session)) -> AuthorPD:
    author = await CRUDBase(Author).get(author_id, session)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.get("/", response_model=list[AuthorPD])
async def get_all(session: AsyncSession = Depends(get_async_session)) -> list[AuthorPD]:
    authors = await CRUDBase(Author).get_all(session)
    if not authors:
        raise HTTPException(status_code=404, detail="Authors not found")
    return authors


@router.post("/", response_model=AuthorPD, response_model_exclude_none=True)
async def create(author: AuthorPD, session: AsyncSession = Depends(get_async_session)):
    return await CRUDBase(Author).create(author, session)


@router.patch("/{author_id}", response_model=AuthorPD)
async def update(author_id: int, obj_in: AuthorPD, session: AsyncSession = Depends(get_async_session)):
    author = CRUDBase(Author)
    author_obj = await author.get(author_id, session)
    if author_obj is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return await author.update(author_obj, obj_in, session)


@router.delete("/{author_id}", response_model=AuthorPD)
async def delete(
    author_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> AuthorPD:

    author = CRUDBase(Author)
    author_obj = await author.get(author_id, session)
    if author_obj is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return await author.remove(author_obj, session)
