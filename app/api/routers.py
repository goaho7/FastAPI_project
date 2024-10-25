from fastapi import APIRouter

from app.api.endpoints import author_router, book_router, tag_router

main_router = APIRouter(prefix="/api")


main_router.include_router(author_router, prefix="/author", tags=["Author"])
main_router.include_router(book_router, prefix="/book", tags=["Book"])
main_router.include_router(tag_router, prefix="/tag", tags=["Tag"])
