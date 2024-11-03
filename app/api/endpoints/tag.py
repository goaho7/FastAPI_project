from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.depensens import tag_service
from app.schemas.tag import TagSchema, TagUpdateSchema
from app.services.tag import TagService

router = APIRouter()


@router.get("/{tag_id}", status_code=status.HTTP_200_OK)
async def get(tag_id: int, service: Annotated[TagService, Depends(tag_service)]) -> TagSchema:
    return await service.get(tag_id)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all(service: Annotated[TagService, Depends(tag_service)]) -> list[TagSchema]:
    return await service.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(book: TagSchema, service: Annotated[TagService, Depends(tag_service)]):
    return await service.create(book)


@router.patch("/{tag_id}", response_model=TagSchema, status_code=status.HTTP_200_OK)
async def update(tag_id: int, data: TagUpdateSchema, service: Annotated[TagService, Depends(tag_service)]):
    return await service.update(data, tag_id)


@router.delete("/{tag_id}")
async def delete(tag_id: int, service: Annotated[TagService, Depends(tag_service)]):
    return await service.remove(tag_id)
