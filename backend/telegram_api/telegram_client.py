import os

from telegram.client import AuthorizationState
from telegram.client import Telegram
from fastapi.exceptions import HTTPException


class TelegramClient(Telegram):
    """Class that overrides the Telegram class.

    Features:
    - Supports credentials with environment variables
    - Non blocking login

    """

    def __init__(self):
        super().__init__(
            api_id=os.environ["TELEGRAM_API_ID"],
            api_hash=os.environ["TELEGRAM_API_HASH"],
            phone=os.environ["TELEGRAM_PHONE"],
            database_encryption_key=os.environ["TELEGRAM_DB_KEY"],
            files_directory=os.environ["TELEGRAM_DIR"],
        )

    def login(
        self, code: str | None = None, password: str | None = None
    ) -> AuthorizationState:
        """Overrides default Telegram login with a non blocking one.

        Args:
            code: A 2FA code sent by Telegram to login.
            password: A password to login.

        Returns:
            The AuthorizationState of the client.

        """

        state = super().login(blocking=False)

        if state == AuthorizationState.WAIT_CODE and code:
            super().send_code(code)

        if state == AuthorizationState.WAIT_PASSWORD and password:
            super().send_password(password)

        return super().login(blocking=False)


def get_client(code: str | None = None, password: str | None = None) -> TelegramClient:
    """Gets a Telegram Client.

    Args:
        code: A 2FA code sent by Telegram to login.
        password: A password to login.

    Returns:
        A Telegram client to make requests.

    Raises:
        HTTPException(403): In case login needs further authentication.

    """

    client = TelegramClient()
    state = client.login(code, password)

    if state == AuthorizationState.WAIT_CODE:
        client.stop()
        raise HTTPException(
            403,
            "Verification code sent. It is needed to complete Telegram authorization",
        )

    if state == AuthorizationState.WAIT_PASSWORD:
        client.stop()
        raise HTTPException(
            403, "Password is needed to complete Telegram authorization"
        )

    if state != AuthorizationState.READY:
        client.stop()
        raise HTTPException(403, "Unauthorized Telegram client")

    return client
