# app/api/endpoints/user.py
from fastapi import APIRouter, HTTPException, Depends, status
from app.core.dependencies import get_current_user
from app.schemas.user_schema import (
    LoginResponse,
    Refresh,
    RefreshResponse,
    UserRegister,
    UserLogin,
    UserResponse,
    PasswordReset,
)
from app.services.user_service import (
    login_user,
    refresh_user,
    register_user,
    get_user_profile,
    reset_password,
)

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def register(user: UserRegister):
    new_user = await register_user(user)
    return new_user


@router.post("/login", response_model=LoginResponse)
async def login(user: UserLogin):
    token = await login_user(user)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials"
        )
    return {
        "access_token": token.get("access_token"),
        "refresh_token": token.get("refresh_token"),
        "token_type": "bearer",
    }


@router.post("/refresh", response_model=RefreshResponse)
async def refresh(data: Refresh):
    token = await refresh_user(data)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials"
        )
    return {
        "access_token": token.get("access_token"),
        "token_type": "bearer",
    }


@router.get("/profile", response_model=UserResponse)
async def profile(current_user: dict = Depends(get_current_user)):
    user = await get_user_profile(current_user["id"])
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


@router.post("/reset-password")
async def reset_password_endpoint(
    reset_data: PasswordReset, current_user: dict = Depends(get_current_user)
):
    success = await reset_password(current_user["id"], reset_data)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Something went Wrong"
        )
    return {"message": "Password reset successfully"}
