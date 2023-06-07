from datetime import timedelta
from fastapi import APIRouter, Depends, Security
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from db.users import get_user
from security import verify_password, manager
from config.settings import settings


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
        data=dict(sub=email),
        expires=settings.access_token_expiration,
        scopes=["auth"]
    )

    refresh_token = manager.create_access_token(
        data=dict(sub=email),
        expires=timedelta(days=15),
        scopes=["refresh"]
    )

    return {
        "access_token": access_token, 
        "token_type": 'Bearer',
        "expires_in": settings.access_token_expiration.seconds,
        "refresh_token": refresh_token
    }

@router.post('/refresh')
async def refresh(user=Security(manager, scopes=["refresh"])):
    
    access_token = manager.create_access_token(
        data=dict(sub=user["email"]),
        expires=settings.access_token_expiration,
        scopes=["auth"]
    )

    return {
        "access_token": access_token, 
        "token_type": 'Bearer',
        "expires_in": settings.access_token_expiration.seconds
    }