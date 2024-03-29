import os
from pymongo.mongo_client import MongoClient

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

mongo_client = MongoClient(f"mongodb://{DB_USER}:{DB_PASS}@social-downloader-db:27017/")
db = mongo_client["social-downloader"]