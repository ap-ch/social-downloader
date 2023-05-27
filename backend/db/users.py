import os
from pymongo.mongo_client import MongoClient
from models.user import UserOut
from security import hash_password

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

mongo_client = MongoClient(f"mongodb://{DB_USER}:{DB_PASS}@social-downloader-db:27017/")
db = mongo_client["social-downloader"]

def get_user(email: str) -> dict:
    return db["users"].find_one({"email": email})

def create_user(email: str, password: str) -> UserOut:
    hashed_pw = hash_password(password)
    user_id = db["users"].insert_one({"email": email, "password": hashed_pw}).inserted_id
    return UserOut(user_id=str(user_id), email=email)