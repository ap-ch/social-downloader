from fastapi import APIRouter, Security
from fastapi.responses import ORJSONResponse
from celery.result import AsyncResult
from celery_tasks import telegram_tasks
from db.results import save_result, get_result
from security import manager

router = APIRouter(prefix="/results")


@router.get("/telegram", response_class=ORJSONResponse)
def result_telegram(task_id: str, user=Security(manager, scopes=["auth"])):
    # Check first if result is stored in the database
    result_value = get_result(task_id, user)
    if not result_value:
        # If not, query Celery
        result = AsyncResult(task_id, app=telegram_tasks.app)
        if not result.ready():
            return {"task_id": result.id, "status": result.status}
        else:
            result_value = result.get()
            save_result(task_id, result_value, user)   
    return ORJSONResponse({"result": result_value})