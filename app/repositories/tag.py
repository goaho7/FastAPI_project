from app.models.tag import AuthorTags, Tag
from app.repositories.base_repository import SQLAlchemyRepository
from app.settings.db import async_session_maker


class TagRepository(SQLAlchemyRepository):
    model = Tag
    model_author_tags = AuthorTags

    async def add_tags_to_author(self, author_id: int, tag_ids: list[int]):
        async with async_session_maker() as session:
            author_tags = [self.model_author_tags(author_id=author_id, tag_id=tag_id) for tag_id in tag_ids]
            session.add_all(author_tags)
            await session.commit()
