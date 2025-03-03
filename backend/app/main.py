from fastapi import FastAPI
from .routers import cohorts

app = FastAPI()

app.include_router(cohorts.router)
