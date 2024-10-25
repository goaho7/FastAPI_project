from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.tag import Tag
from app.schemas.tag import Tag as TagPD
from app.settings.db import get_async_session

router = APIRouter()


@router.get("/{book_id}", response_model=TagPD)
async def get(book_id: int, session: AsyncSession = Depends(get_async_session)) -> TagPD:
    tag = await CRUDBase(Tag).get(book_id, session)
    if tag is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return tag


@router.get("/", response_model=list[TagPD])
async def get_all(session: AsyncSession = Depends(get_async_session)) -> list[TagPD]:
    tags = await CRUDBase(Tag).get_all(session)
    if tags is None:
        raise HTTPException(status_code=404, detail="Books not found")
    return tags
