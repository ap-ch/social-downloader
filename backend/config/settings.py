from pydantic import BaseSettings


class Settings(BaseSettings):
    secret: str


settings = Settings()
