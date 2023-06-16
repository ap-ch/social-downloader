from fastapi import APIRouter, Security
from telegram_api import telegram_client
from models.telegram import MessagesIn
from celery_tasks import telegram_tasks
from db.tasks import save_task
from security import manager

router = APIRouter(prefix="/telegram")


@router.get("/login")
def telegram_login(
    user=Security(manager, scopes=["auth"]),
    code: str | None = None,
    password: str | None = None
):
    client = telegram_client.get_client(user, code, password)
    if isinstance(client, telegram_client.TelegramClient):
        client.stop()
        return {"message": "Telegram client was authorized successfully"}
    else:
        return {"message": "Something went wrong! Telegram client is not authorized"}


@router.get("/chats")
def telegram_chats(user=Security(manager, scopes=["auth"])):
    result = telegram_tasks.get_chats_task.delay(user)
    save_task(
        result.id,
        "telegram",
        "chats",
        user
    )
    return {"task_id": result.id}


@router.get("/chats-name")
def telegram_chats_name(user=Security(manager, scopes=["auth"])):
    result = telegram_tasks.get_chats_name_task.delay(user)
    save_task(
        result.id,
        "telegram",
        "chats_name",
        user
    )
    return {"task_id": result.id}


@router.get("/chat")
def telegram_chat(chat_id: int, user=Security(manager, scopes=["auth"])):
    result = telegram_tasks.get_chat_task.delay(user, chat_id)
    save_task(
        result.id,
        "telegram",
        "chat",
        user
    )
    return {"task_id": result.id}


@router.get("/search-public-chats")
def telegram_search_public_chats(query: str, user=Security(manager, scopes=["auth"])):
    result = telegram_tasks.search_public_chats_task.delay(user, query)
    save_task(
        result.id,
        "telegram",
        "search-public-chats",
        user
    )
    return {"task_id": result.id}


@router.get("/search-public-chats-name")
def telegram_search_public_chats_name(query: str, user=Security(manager, scopes=["auth"])):
    result = telegram_tasks.search_public_chats_name_task.delay(user, query)
    save_task(
        result.id,
        "telegram",
        "search-public-chats-name",
        user
    )
    return {"task_id": result.id}


@router.get("/messages")
def telegram_messages(
    chat_id: int, 
    limit: int | None = None,
    user=Security(manager, scopes=["auth"])
):
    result = telegram_tasks.get_messages_task.delay(user, chat_id, limit)
    save_task(
        result.id,
        "telegram",
        "messages",
        user
    )
    return {"task_id": result.id}


@router.get("/me")
def telegram_me(user=Security(manager, scopes=["auth"])):
    result = telegram_tasks.get_me_task.delay(user)
    save_task(
        result.id,
        "telegram",
        "me",
        user
    )
    return {"task_id": result.id}
