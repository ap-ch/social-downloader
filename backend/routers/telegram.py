from fastapi import APIRouter
from celery.result import AsyncResult
from celery_tasks import telegram_tasks

router = APIRouter(prefix="/telegram")


@router.get("/login")
def telegram_login(code: str | None = None, password: str | None = None):
    result = telegram_tasks.login_task.delay(code, password)
    return {"task_id": result.id}


@router.get("/result")
def telegram_result(task_id: str):
    result = AsyncResult(task_id, app=telegram_tasks.app)
    if not result.ready():
        return {"task_id": result.id, "status": result.status}
    else:
        return {"result": result.get()}


@router.get("/chats")
def telegram_chats():
    result = telegram_tasks.get_chats_task.delay()
    return {"task_id": result.id}


@router.get("/chats/{chat_id}")
def telegram_chat(chat_id: int):
    result = telegram_tasks.get_chat_task.delay(chat_id)
    return {"task_id": result.id}


@router.get("/messages/{chat_id}")
def telegram_messages(chat_id: int, limit: int | None = None):
    result = telegram_tasks.get_messages_task.delay(chat_id, limit)
    return {"task_id": result.id}


@router.get("/me")
def telegram_me():
    result = telegram_tasks.get_me_task.delay()
    return {"task_id": result.id}
