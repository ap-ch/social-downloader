from telegram_api.telegram_client import TelegramClient

def get_chats() -> dict:
    """Gets Telegram chats"""

    client = TelegramClient()
    client.login()

    result = client.get_chats()
    result.wait()
    chats = result.update

    client.stop()

    return chats

def get_chat(chat_id: int):
    """Gets a Telegram chat with its id"""

    client = TelegramClient()
    client.login()

    result = client.get_chat(chat_id)
    result.wait()
    chat = result.update

    client.stop()

    return chat
