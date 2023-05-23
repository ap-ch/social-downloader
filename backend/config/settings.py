from pydantic import BaseSettings


class Settings(BaseSettings):
    auth_secret: str


settings = Settings()
