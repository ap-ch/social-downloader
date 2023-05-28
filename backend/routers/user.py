from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from models.user import UserIn, UserOut
from db.users import create_user


router = APIRouter(prefix="/user")


@router.post("/register", status_code=201)
def register(user: UserIn) -> UserOut:
    try:
        user = create_user(user.email, user.password)
        return user
    except:
        raise HTTPException(status_code=400, detail="Could not create User")
