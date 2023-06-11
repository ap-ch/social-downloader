from bson.objectid import ObjectId
from db.db import db

def get_user_preferences(user) -> dict:
    return db["preferences"].find_one(
        {"user_id": ObjectId(user["id"])}, 
        {"_id": 0, "user_id": 0}
    )

def set_telegram_phone(telegram_phone: str, user):
    db["preferences"].update_one(
        {"user_id": ObjectId(user["id"])},
        {"$set": {
            "telegram_login": {
                "phone": telegram_phone
            }
        }},
        upsert=True
    )

def set_telegram_bot_token(telegram_bot_token: str, user):
    db["preferences"].update_one(
        {"user_id": ObjectId(user["_id"])},
        {"$set": {
            "telegram_login": {
                "bot_token": telegram_bot_token
            }
        }},
        upsert=True
    )