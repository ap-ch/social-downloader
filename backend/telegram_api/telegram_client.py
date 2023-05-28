import os
from telegram.client import AuthorizationState
from telegram.client import Telegram
from fastapi.exceptions import HTTPException
from db.preferences import get_user_preferences


class TelegramClient(Telegram):
    """Class that overrides the Telegram class.

    Features:
    - Supports credentials with environment variables
    - Non blocking login

    """

    def __init__(
        self, 
        telegram_prefs
    ):
        self.phone = telegram_prefs["phone"] \
            if "phone" in telegram_prefs else None
        self.bot_token = telegram_prefs["bot_token"] \
            if "bot_token" in telegram_prefs else None

        if self.phone:
            super().__init__(
                api_id=os.environ["TELEGRAM_API_ID"],
                api_hash=os.environ["TELEGRAM_API_HASH"],
                phone=self.phone,
                database_encryption_key=os.environ["TELEGRAM_DB_KEY"],
                files_directory=os.environ["TELEGRAM_DIR"] + f"phone_{self.phone}/",
            )

        elif self.bot_token:
            super().__init__(
                api_id=os.environ["TELEGRAM_API_ID"],
                api_hash=os.environ["TELEGRAM_API_HASH"],
                bot_token=self.bot_token,
                database_encryption_key=os.environ["TELEGRAM_DB_KEY"],
                files_directory=os.environ["TELEGRAM_DIR"] + f"bot_{self.phone}/",
            )

    def login(
        self,
        code: str | None = None,
        password: str | None = None
    ) -> AuthorizationState:
        """Overrides default Telegram login with a non blocking one.

        Args:
            code: A 2FA code sent by Telegram to login.
            password: A password to login.

        Returns:
            The AuthorizationState of the client.

        """

        if self.phone:      
            # Phone authorization requires a code and a password
            state = super().login(blocking=False)
            
            if state == AuthorizationState.WAIT_CODE and code:
                try:
                    super().send_code(code)
                except RuntimeError:
                    return AuthorizationState.NONE

            if state == AuthorizationState.WAIT_PASSWORD and password:
                try:
                    super().send_password(password)
                except RuntimeError:
                    return AuthorizationState.NONE

        return super().login(blocking=False)


def get_client(
    user,
    code: str | None = None,
    password: str | None = None
) -> TelegramClient:
    """Gets a Telegram Client.

    Args:
        user: An authenticated user.
        code: A 2FA code sent by Telegram to login.
        password: A password to login.

    Returns:
        A Telegram client to make requests.

    Raises:
        HTTPException(403): In case login needs further authentication.

    """

    try:
        telegram_prefs = get_user_preferences(user)["telegram_login"]
    except (TypeError, KeyError):
        raise HTTPException(status_code=400, detail="User does not have preferences defined")

    try:
        client = TelegramClient(telegram_prefs)
    except:
        raise HTTPException(status_code=400, detail="Could not get Telegram client")
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
            403,
            "Password is needed to complete Telegram authorization"
        )

    if state != AuthorizationState.READY:
        client.stop()
        raise HTTPException(403, "Unauthorized Telegram client")

    return client
