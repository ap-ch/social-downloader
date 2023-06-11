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

def get_user_tasks(user, task_type: str):
    all_user_tasks = db["tasks"].find_one(
        {"user_id": ObjectId(user["id"])}, 
        {"_id": 0, "user_id": 0}
    )["tasks"]
    type_tasks = [
        {
            "task_id": task["task_id"],
            "task_detail": task["task_detail"],
            "date_created": task["date_created"]
        }
        for task in all_user_tasks
        if task["task_type"] == task_type
    ]
    return type_tasks

def delete_user_task(user, task_id: str):
    db["tasks"].update_one(
        {"user_id": ObjectId(user["id"])},
        {
        "$pull": {
            "tasks": {
                "task_id": task_id
            }
        }
        }
    )