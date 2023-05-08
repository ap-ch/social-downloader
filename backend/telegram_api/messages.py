import time

from telegram_api.telegram_client import get_client


def get_messages(chat_id: int, limit: int | None = None) -> list[dict]:
    """Handles Telegram chat history pagination and returns N messages.

    Args:
        chat_id: ID for a chat.
        limit: The number of messages to return, or None for all messages.

    Returns:
        A list of messages sorted by date in descending order.

    """

    client = get_client()

    messages_list = []

    result = client.get_chat_history(chat_id)
    result.wait()
    chat_history = result.update
    messages = chat_history["messages"]
    last_message = messages[0]
    messages_list.append(last_message)

    end_of_messages = False
    while not end_of_messages and (len(messages_list) < limit if limit else True):
        result = client.get_chat_history(
            chat_id, limit=100, from_message_id=last_message["id"]
        )
        result.wait()
        chat_history = result.update
        messages = chat_history["messages"]
        if messages:
            messages_list.extend(messages)
            last_message = messages[-1]
            time.sleep(0.25)  # little delay to not flood the API
        else:
            end_of_messages = True

    client.stop()

    return messages_list[0:limit]
