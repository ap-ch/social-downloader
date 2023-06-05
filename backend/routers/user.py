from fastapi import APIRouter, Security
from fastapi.exceptions import HTTPException
from models.user import UserIn, UserOut
from db.users import create_user
from security import manager


router = APIRouter(prefix="/user")

@router.get("/", status_code=200)
def info(user=Security(manager, scopes=["auth"])) -> UserOut:
    return UserOut(user_id=user["id"], email=user["email"])

@router.post("/register", status_code=201)
def register(user: UserIn) -> UserOut:
    try:
        user = create_user(user.email, user.password)
        return user
    except:
        raise HTTPException(status_code=400, detail="Could not create User")
