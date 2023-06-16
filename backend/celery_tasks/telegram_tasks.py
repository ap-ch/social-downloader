import config.celery_config as celery_config
from celery import Celery
from telegram_api import chats, messages, users

app = Celery(__name__, broker=celery_config.broker_url)
app.conf.update(result_backend=celery_config.result_backend)


@app.task(name="telegram:get_chats", max_retries=5)
def get_chats_task(user):
    return chats.get_chats(user)


@app.task(name="telegram:get_chats_name", max_retries=5)
def get_chats_name_task(user):
    return chats.get_chats_name(user)


@app.task(name="telegram:get_chat", max_retries=5)
def get_chat_task(user, chat_id: int):
    chat = chats.get_chat(user, chat_id)
    if not chat:
        # TDLib needs to have chats cached before getting a chat
        _ = chats.get_chats(user)
        chat = chats.get_chat(user, chat_id)
    return chat


@app.task(name="telegram:search_public_chats", max_retries=5)
def search_public_chats_task(user, query: str):
    return chats.search_public_chats(user, query)


@app.task(name="telegram:search_public_chats_name", max_retries=5)
def search_public_chats_name_task(user, query: str):
    return chats.search_public_chats_name(user, query)


@app.task(name="telegram:get_messages_task", max_retries=5)
def get_messages_task(user, chat_id: int, limit: int | None = None) -> list[dict]:
    return messages.get_messages(user, chat_id, limit)


@app.task(name="telegram:get_me_task", max_retries=5)
def get_me_task(user) -> list[dict]:
    return users.get_me(user)
