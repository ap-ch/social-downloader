from fastapi import APIRouter, Security
from fastapi.exceptions import HTTPException
from db.preferences import (
    set_telegram_phone,
    set_telegram_bot_token
)
from security import manager


router = APIRouter(prefix="/preferences")


@router.post("/telegram_login", status_code=201)
def set_preferences_telegram_login(
    phone: str | None = None, 
    bot_token: str | None = None,
    user=Security(manager, scopes=["auth"])
):
    try:
        if phone:
            set_telegram_phone(phone, user)
        elif bot_token:
            set_telegram_bot_token(bot_token, user)
        else:
            raise HTTPException(
                status_code=400, 
                detail="A phone number or a bot token is required"
            )
        return {"message": "Preferences updated"}
    except:
        raise HTTPException(status_code=400, detail="Could not update preferences")

