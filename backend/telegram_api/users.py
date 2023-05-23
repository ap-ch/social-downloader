from telegram_api.telegram_client import get_client


def get_me() -> dict:
    """Gets your Telegram user"""

    client = get_client()

    result = client.call_method("getMe")
    result.wait()
    me = result.update

    client.stop()

    return me
