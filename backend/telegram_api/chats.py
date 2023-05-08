from telegram_api.telegram_client import get_client


def get_chats() -> dict:
    """Gets Telegram chats"""

    client = get_client()

    result = client.get_chats()
    result.wait()
    chats = result.update

    client.stop()

    return chats


def get_chat(chat_id: int):
    """Gets a Telegram chat with its id"""

    client = get_client()

    result = client.get_chat(chat_id)
    result.wait()
    chat = result.update

    client.stop()

    return chat
