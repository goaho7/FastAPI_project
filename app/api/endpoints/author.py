from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.depensens import author_service
from app.schemas.author import AuthorSchema, AuthorUpdateSchema
from app.services.author import AuthorService

router = APIRouter()


@router.get("/{author_id}", status_code=status.HTTP_200_OK)
async def get(author_id: int, service: Annotated[AuthorService, Depends(author_service)]) -> AuthorSchema:
    return await service.get(author_id)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all(service: Annotated[AuthorService, Depends(author_service)]) -> list[AuthorSchema]:
    return await service.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(author: AuthorSchema, service: Annotated[AuthorService, Depends(author_service)]):
    return await service.create(author)


@router.patch("/{author_id}", response_model=AuthorSchema, status_code=status.HTTP_200_OK)
async def update(author_id: int, data: AuthorUpdateSchema, service: Annotated[AuthorService, Depends(author_service)]):
    return await service.update(data, author_id)


@router.delete("/{author_id}")
async def delete(author_id: int, service: Annotated[AuthorService, Depends(author_service)]):
    return await service.remove(author_id)
