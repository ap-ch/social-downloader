from models.user import UserOut
from security import hash_password
from db.db import db

def get_user(email: str) -> dict:
    user = db["users"].find_one({"email": email})
    if not user:
        return None
    user["id"] = str(user["_id"])
    user["_id"] = None
    return user


def create_user(email: str, password: str) -> UserOut:
    hashed_pw = hash_password(password)
    user_id = db["users"].insert_one({"email": email, "password": hashed_pw}).inserted_id
    return UserOut(user_id=str(user_id), email=email)
