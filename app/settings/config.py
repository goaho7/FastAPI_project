from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ASYNC_POSTGRES_CONNECT: str = None
    POSTGRES_DB: str = None
    POSTGRES_USER: str = None
    POSTGRES_PASSWORD: str = None
    POSTGRES_HOST_NAME: str = None
    POSTGRES_PORT: int = None

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
