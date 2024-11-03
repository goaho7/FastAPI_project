from app.models.author import Author
from app.repositories.base_repository import SQLAlchemyRepository


class AuthorRepository(SQLAlchemyRepository):
    model = Author
