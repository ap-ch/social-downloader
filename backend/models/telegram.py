from pydantic import BaseModel

class TelegramLoginIn(BaseModel):
    phone: str | None = None
    bot_token: str | None = None

class MessagesIn(BaseModel):
    limit: int