# app/services/user_service.py
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_refresh_token,
)
from app.models.user_model import User
from app.schemas.user_schema import Refresh, UserRegister, UserLogin, PasswordReset
from tortoise.exceptions import DoesNotExist
from passlib.context import CryptContext
from passlib.hash import sha512_crypt


pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return sha512_crypt.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return sha512_crypt.verify(plain_password, hashed_password)


async def register_user(user_data: UserRegister) -> User:
    hashed_password = hash_password(user_data.password)
    user = await User.create(
        name=user_data.name,
        username=user_data.username,
        email=user_data.email,
        password=hashed_password,
    )
    return user


async def authenticate_user(username: str, password: str) -> User | None:
    try:
        user = await User.get(username=username)
        if verify_password(password, user.password):
            return user
    except DoesNotExist:
        return None
    return None


async def get_user_profile(user_id: int) -> User | None:
    return await User.get(id=user_id)


async def reset_password(user_id: int, reset_data: PasswordReset) -> bool:
    try:
        user = await User.get(id=user_id)
        if verify_password(reset_data.old_password, user.password):
            user.password = hash_password(reset_data.new_password)
            await user.save()
            return True
        return False
    except DoesNotExist:
        return False


async def login_user(user_data: UserLogin) -> dict[str, str] | None:
    user = await authenticate_user(user_data.username, user_data.password)
    if user:
        token = create_access_token({"sub": user.id})
        refresh_token = create_refresh_token({"sub": user.id})
        return {"access_token": token, "refresh_token": refresh_token}
    return None


async def refresh_user(data: Refresh) -> dict[str, str] | None:
    payload = decode_refresh_token(data.refresh_token)
    if not payload:
        return None
    user = await get_user_profile(payload.get("sub"))
    if user:
        token = create_access_token({"sub": user.id})
        return {"access_token": token}
    return None
