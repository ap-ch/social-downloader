import re
from fastapi import APIRouter, Security
from fastapi.exceptions import HTTPException
from models.telegram import TelegramLoginIn
from db.preferences import (
    set_telegram_phone,
    set_telegram_bot_token,
    get_user_preferences
)
from security import manager


router = APIRouter(prefix="/preferences")

@router.get("/", status_code=200)
def get_preferences(
    user=Security(manager, scopes=["auth"])
):
    user_preferences = get_user_preferences(user)
    if user_preferences:
        return user_preferences
    else:
        raise HTTPException(
            status_code=404, 
            detail="Not found"
        )

@router.get("/telegram_login", status_code=200)
def get_preferences_telegram_login(
    user=Security(manager, scopes=["auth"])
):
    user_preferences = get_user_preferences(user)
    if user_preferences and 'telegram_login' in user_preferences:
        telegram_preferences = user_preferences['telegram_login']
        return telegram_preferences
    else:
        raise HTTPException(
            status_code=404, 
            detail="Not found"
        )

@router.post("/telegram_login", status_code=201)
def set_preferences_telegram_login(
    telegram_login: TelegramLoginIn,
    user=Security(manager, scopes=["auth"])
):
    try:
        if telegram_login.phone:
            if not re.search(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$",  telegram_login.phone):
                raise HTTPException(status_code=422, detail="Invalid phone format")
            set_telegram_phone(telegram_login.phone, user)
        elif telegram_login.bot_token:
            set_telegram_bot_token(telegram_login.bot_token, user)
        else:
            raise HTTPException(
                status_code=400, 
                detail="A phone number or a bot token is required"
            )
        return {"message": "Preferences updated"}
    except Exception as exc:
        raise exc

