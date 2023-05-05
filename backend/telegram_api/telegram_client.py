import os

from telegram.client import AuthorizationState
from telegram.client import Telegram

class TelegramClient(Telegram):
    """Class that overrides the Telegram class.
    
    Features:
    - Supports credentials with environment variables
    - Non blocking login
    
    """

    def __init__(self):
        super().__init__(
            api_id=os.environ['TELEGRAM_API_ID'],
            api_hash=os.environ['TELEGRAM_API_HASH'],
            phone=os.environ["TELEGRAM_PHONE"],
            database_encryption_key=os.environ["TELEGRAM_DB_KEY"],
            files_directory=os.environ["TELEGRAM_DIR"]
        )

    def login(self):
        """Overrides default Telegram login with a non blocking one"""

        state = super().login(blocking=False)

        if state == AuthorizationState.WAIT_CODE:
            code = input("Input code: ")
            super().send_code(code)

        if state == AuthorizationState.WAIT_PASSWORD:
            password = input("Input password: ")
            super().send_password(password)
        
        state = super().login(blocking=False)

