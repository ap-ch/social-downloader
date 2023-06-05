from datetime import timedelta
from pydantic import BaseSettings


class Settings(BaseSettings):
    secret: str
    access_token_expiration: timedelta = timedelta(minutes=15)


settings = Settings()
