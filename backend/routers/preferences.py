from fastapi import APIRouter, Security
from fastapi.exceptions import HTTPException
from db.preferences import (
    set_telegram_phone,
    set_telegram_bot_token,
    get_user_preferences
)
from security import manager


router = APIRouter(prefix="/preferences")

@router.get("/telegram_login", status_code=200)
def get_preferences_telegram_login(
    user=Security(manager, scopes=["auth"])
):
    user_preferences = get_user_preferences(user)
    if 'telegram_login' in user_preferences:
        telegram_preferences = user_preferences['telegram_login']
        return telegram_preferences
    else:
        raise HTTPException(
            status_code=404, 
            detail="Not found"
        )

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

