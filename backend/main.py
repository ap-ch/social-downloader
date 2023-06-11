from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, user, preferences, telegram, services, results, tasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(results.router)
app.include_router(services.router)
app.include_router(preferences.router)
app.include_router(tasks.router)
app.include_router(telegram.router)
