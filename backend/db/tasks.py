from bson.objectid import ObjectId
from datetime import datetime
from db.db import db

def save_task(task_id: str, task_type: str, task_detail: str, user):
    db["tasks"].update_one(
        {"user_id": ObjectId(user["id"])},
        {"$push": {
            "tasks": {
                "task_id": task_id,
                "task_type": task_type,
                "task_detail": task_detail,
                "date_created": datetime.utcnow()
            }
        }},
        upsert=True
    )