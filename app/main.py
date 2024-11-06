from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.core.config import settings
from app.api.endpoints import users_router
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.include_router(users_router.router, prefix="/users", tags=["users"])

register_tortoise(
    app,
    db_url=settings.DATABASE_URL,
    modules={"models": ["app.models.user_model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

# Entry point for running the server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
