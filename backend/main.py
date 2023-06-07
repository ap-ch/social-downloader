from fastapi import FastAPI
from routers import auth, user, preferences, telegram, services, results

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(results.router)
app.include_router(services.router)
app.include_router(preferences.router)
app.include_router(telegram.router)
