from fastapi import FastAPI
from routers import telegram

app = FastAPI()

app.include_router(telegram.router)
