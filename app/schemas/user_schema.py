# app/schemas/user.py
from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Refresh(BaseModel):
    refresh_token: str


class UserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    is_admin: bool
    is_verify: bool

    class Config:
        from_attributes = True


class PasswordReset(BaseModel):
    old_password: str
    new_password: str


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class RefreshResponse(BaseModel):
    access_token: str
    token_type: str
