from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from config.settings import settings
from db.users import get_user
from security import verify_password, manager


router = APIRouter(prefix="/auth")


@manager.user_loader()
def load_user(email: str):
    user = get_user(email)
    return user

@router.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username

    user = load_user(email)
    if not user:
        raise InvalidCredentialsException
    if not verify_password(form_data.password, user['password']):
        raise InvalidCredentialsException
    
    access_token = manager.create_access_token(
        data=dict(sub=email)
    )
    return {"access_token": access_token, "token_type": 'bearer'}