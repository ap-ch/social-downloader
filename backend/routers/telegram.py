from fastapi import APIRouter, Security
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
    result = telegram_tasks.login_task.delay(user, code, password)
    return {"task_id": result.id}


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


@router.get("/chats/{chat_id}")
def telegram_chat(chat_id: int, user=Security(manager, scopes=["auth"])):
    result = telegram_tasks.get_chat_task.delay(user, chat_id)
    save_task(
        result.id,
        "telegram",
        "chat",
        user
    )
    return {"task_id": result.id}


@router.get("/messages/{chat_id}")
def telegram_messages(chat_id: int, user=Security(manager, scopes=["auth"]), limit: MessagesIn | None = None):
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
