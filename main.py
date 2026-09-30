from fastapi import FastAPI

from src.base.exception_handlers import register_exception_handlers
from src.routers import user

app = FastAPI()

register_exception_handlers(app)

app.include_router(user.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
