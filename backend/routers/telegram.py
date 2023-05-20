from fastapi import APIRouter, HTTPException

from telegram_api.telegram_client import TelegramClient, get_client
from telegram_api.chats import get_chats, get_chat
from telegram_api.messages import get_messages
from telegram_api.users import get_me

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World!"}


@router.get("/telegram/login")
async def telegram_login(code: str | None = None, password: str | None = None):
    client = get_client(code, password)
    if isinstance(client, TelegramClient):
        client.stop()
        return {"message": "Telegram client was authorized successfully"}
    else:
        return {"message": "Something went wrong! Telegram client is not authorized"}


@router.get("/telegram/chats")
async def telegram_chats():
    chats = get_chats()
    return chats


@router.get("/telegram/chats/{chat_id}")
async def telegram_chat(chat_id: int):
    chat = get_chat(chat_id)
    if not chat:
        # TDLib needs to have chats cached before getting a chat
        _ = get_chats()
        chat = get_chat(chat_id)
        if not chat:
            raise HTTPException(status_code=404, detail="Chat not found")
    return chat


@router.get("/telegram/messages/{chat_id}")
async def telegram_messages(chat_id: int, limit: int | None = None):
    messages = get_messages(chat_id, limit)
    return messages

@router.get("/telegram/me")
async def telegram_me():
    me = get_me()
    return me
