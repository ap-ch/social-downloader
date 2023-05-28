from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import ORJSONResponse
from celery.result import AsyncResult
from celery_tasks import telegram_tasks
from db.preferences import get_user_preferences
from db.tasks import save_task
from db.results import save_result, get_result
from security import manager

router = APIRouter(prefix="/telegram")


@router.get("/result", response_class=ORJSONResponse)
def telegram_result(task_id: str, user=Depends(manager)):
    # Check first if result is stored in the database
    result_value = get_result(task_id, user)
    if not result_value:
        # If not, query Celery
        result = AsyncResult(task_id, app=telegram_tasks.app)
        if not result.ready():
            return {"task_id": result.id, "status": result.status}
        else:
            result_value = result.get()
            save_result(task_id, result_value, user)   
    return ORJSONResponse({"result": result_value})


@router.get("/login")
def telegram_login(
    user=Depends(manager),
    code: str | None = None,
    password: str | None = None
):
    result = telegram_tasks.login_task.delay(user, code, password)
    return {"task_id": result.id}


@router.get("/chats")
def telegram_chats(user=Depends(manager)):
    result = telegram_tasks.get_chats_task.delay(user)
    save_task(
        result.id,
        "telegram",
        "chats",
        user
    )
    return {"task_id": result.id}


@router.get("/chats/{chat_id}")
def telegram_chat(chat_id: int, user=Depends(manager)):
    result = telegram_tasks.get_chat_task.delay(user, chat_id)
    save_task(
        result.id,
        "telegram",
        "chat",
        user
    )
    return {"task_id": result.id}


@router.get("/messages/{chat_id}")
def telegram_messages(chat_id: int, user=Depends(manager), limit: int | None = None):
    result = telegram_tasks.get_messages_task.delay(user, chat_id, limit)
    save_task(
        result.id,
        "telegram",
        "messages",
        user
    )
    return {"task_id": result.id}


@router.get("/me")
def telegram_me(user=Depends(manager)):
    result = telegram_tasks.get_me_task.delay(user)
    save_task(
        result.id,
        "telegram",
        "me",
        user
    )
    return {"task_id": result.id}
