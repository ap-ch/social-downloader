import time
from telegram_api.telegram_client import get_client

def get_chats(user) -> dict:
    """Gets Telegram chats"""

    client = get_client(user)

    result = client.get_chats()
    result.wait()
    chats = result.update

    client.stop()

    return chats

def get_chats_name(user) -> dict:
    """Gets Telegram chats, returned along along with their display name"""

    client = get_client(user)

    result = client.get_chats()
    result.wait()
    chats = result.update

    chats_name = {}
    chats_name["total_count"] = chats["total_count"]
    chats_name["chats"] = []

    for chat_id in chats["chat_ids"]:
        result = client.get_chat(chat_id)
        result.wait()
        chat = result.update
        chats_name["chats"].append(
            {"id": chat_id, "name": chat["title"]}
        )
        time.sleep(0.25)

    client.stop()

    return chats_name

def search_public_chats(user, query: str) -> dict:
    """Search Telegram public chats given a query"""

    client = get_client(user)

    result = client.call_method("searchPublicChats", {"query": query})
    result.wait()
    public_chats = result.update

    client.stop()

    return public_chats

def search_public_chats_name(user, query: str) -> dict:
    """Search public Telegram chats by a keyword, returned along with their display name"""

    client = get_client(user)

    result = client.call_method("searchPublicChats", {"query": query})
    result.wait()
    chats = result.update

    chats_name = {}
    chats_name["total_count"] = chats["total_count"]
    chats_name["chats"] = []

    for chat_id in chats["chat_ids"]:
        result = client.get_chat(chat_id)
        result.wait()
        chat = result.update
        chats_name["chats"].append(
            {"id": chat_id, "name": chat["title"]}
        )
        time.sleep(0.25)

    client.stop()

    return chats_name

def get_chat(user, chat_id: int):
    """Gets a Telegram chat with its id"""

    client = get_client(user)

    result = client.get_chat(chat_id)
    result.wait()
    chat = result.update

    client.stop()

    return chat
