import config.celery_config as celery_config
from fastapi.exceptions import HTTPException
from celery import Celery
from telegram_api import telegram_client, chats, messages, users

app = Celery(__name__, broker=celery_config.broker_url)
app.conf.update(result_backend=celery_config.result_backend)


""" @app.task(name="telegram:login")
def login_task(
    user,
    code: str | None = None,
    password: str | None = None
):
    
    client = telegram_client.get_client(user, code, password)
    if isinstance(client, telegram_client.TelegramClient):
        client.stop()
        return {"message": "Telegram client was authorized successfully"}
    else:
        return {"message": "Something went wrong! Telegram client is not authorized"} """


@app.task(name="telegram:get_chats")
def get_chats_task(user):
    try:
        return chats.get_chats(user)
    except Exception as exc:
        raise HTTPException(*exc.args)


@app.task(name="telegram:get_chat")
def get_chat_task(user, chat_id: int):
    try:
        chat = chats.get_chat(user, chat_id)
        if not chat:
            # TDLib needs to have chats cached before getting a chat
            _ = chats.get_chats(user)
            chat = chats.get_chat(user, chat_id)
        return chat
    except Exception as exc:
        raise HTTPException(*exc.args)


@app.task(name="telegram:get_messages_task")
def get_messages_task(user, chat_id: int, limit: int | None = None) -> list[dict]:
    try:
        return messages.get_messages(user, chat_id, limit)
    except Exception as exc:
        raise HTTPException(*exc.args)


@app.task(name="telegram:get_me_task")
def get_me_task(user) -> list[dict]:
    try:
        return users.get_me(user)
    except Exception as exc:
        raise HTTPException(*exc.args)
