from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.tag import Tag
from app.schemas.tag import Tag as TagPD
from app.settings.db import get_async_session

router = APIRouter()


@router.get("/{tag_id}", response_model=TagPD)
async def get(tag_id: int, session: AsyncSession = Depends(get_async_session)) -> TagPD:
    tag = await CRUDBase(Tag).get(tag_id, session)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


@router.get("/", response_model=list[TagPD])
async def get_all(session: AsyncSession = Depends(get_async_session)) -> list[TagPD]:
    tags = await CRUDBase(Tag).get_all(session)
    if tags is None:
        raise HTTPException(status_code=404, detail="Tags not found")
    return tags


@router.post("/", response_model=TagPD, response_model_exclude_none=True)
async def create(tag: TagPD, session: AsyncSession = Depends(get_async_session)):
    return await CRUDBase(Tag).create(tag, session)


@router.patch("/{tag_id}", response_model=TagPD)
async def update(tag_id: int, obj_in: TagPD, session: AsyncSession = Depends(get_async_session)):
    tag = CRUDBase(Tag)
    tag_obj = await tag.get(tag_id, session)
    if tag_obj is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return await tag.update(tag_obj, obj_in, session)


@router.delete("/{tag_id}", response_model=TagPD)
async def delete(
    tag_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> TagPD:

    tag = CRUDBase(Tag)
    tag_obj = await tag.get(tag_id, session)
    if tag_obj is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return await tag.remove(tag_obj, session)
