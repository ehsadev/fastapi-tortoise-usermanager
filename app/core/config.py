# app/core/config.py
from pydantic_settings import BaseSettings
from os import getenv


class Settings(BaseSettings):
    DATABASE_URL: str = getenv(
        key="DATABASE_URI", default="postgres://user:password@localhost:5432/mydatabase"
    )
    JWT_SECRET_KEY: str = getenv("ACCESS_TOKEN_SECRET_KEY", "your_secret_key")
    JWT_REFRESH_SECRET_KEY: str = getenv("REFRESH_TOKEN_SECRET_KEY", "your_secret_key")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 30
    JWT_REFRESH_EXPIRATION_DAYS: int = 1


settings = Settings()
