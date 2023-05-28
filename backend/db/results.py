from bson.objectid import ObjectId
from db.db import db

def save_result(task_id: str, result: list | dict, user):
    db["results"].update_one(
        {"user_id": ObjectId(user["id"])},
        {"$set": {f"results.{task_id}": result}},
        upsert=True
    )

def get_result(task_id: str, user) -> list | dict:
    user_results = db["results"].find_one({"user_id": ObjectId(user["id"])}, {"_id": 0})
    if user_results:
        if task_id in user_results["results"]:
            return user_results["results"][task_id]
    return None