import config.celery_config as celery_config
from celery import Celery
from telegram_api import telegram_client, chats, messages, users

app = Celery(__name__, broker=celery_config.broker_url)
app.conf.update(result_backend=celery_config.result_backend)


@app.task(name="telegram:login")
def login_task(code: str | None = None, password: str | None = None):
    client = telegram_client.get_client(code, password)
    if isinstance(client, telegram_client.TelegramClient):
        client.stop()
        return {"message": "Telegram client was authorized successfully"}
    else:
        return {"message": "Something went wrong! Telegram client is not authorized"}


@app.task(name="telegram:get_chats")
def get_chats_task():
    return chats.get_chats()


@app.task(name="telegram:get_chat")
def get_chat_task(chat_id: int):
    chat = chats.get_chat(chat_id)
    if not chat:
        # TDLib needs to have chats cached before getting a chat
        _ = chats.get_chats()
        chat = chats.get_chat(chat_id)
    return chat


@app.task(name="telegram:get_messages_task")
def get_messages_task(chat_id: int, limit: int | None = None) -> list[dict]:
    return messages.get_messages(chat_id, limit)


@app.task(name="telegram:get_me_task")
def get_me_task() -> list[dict]:
    return users.get_me()
