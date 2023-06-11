import re
from fastapi import APIRouter, Security
from fastapi.exceptions import HTTPException
from models.telegram import TelegramLoginIn
from db.tasks import get_user_tasks, delete_user_task
from security import manager


router = APIRouter(prefix="/tasks")

@router.get("/", status_code=200)
def get_tasks(
    task_type: str,
    user=Security(manager, scopes=["auth"])
):
    user_tasks = get_user_tasks(user, task_type)
    if user_tasks:
        return user_tasks
    else:
        raise HTTPException(
            status_code=404, 
            detail="Not found"
        )
    
@router.get("/delete/{task_id}", status_code=200)
def delete_task(
    task_id: str,
    user=Security(manager, scopes=["auth"])
):
    try:
        delete_user_task(user, task_id)
        return {"detail": f"Deleted task {task_id}"}
    except:
        raise HTTPException(
            status_code=400, 
            detail="Could not delete task"
        )

