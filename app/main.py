from fastapi import FastAPI
from app.auth import auth_router
from app.tasks import tasks_router

app = FastAPI()

# Include Routers for Authentication and Task Management
app.include_router(auth_router)
app.include_router(tasks_router)
