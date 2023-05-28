from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    user_id: str
    email: EmailStr
