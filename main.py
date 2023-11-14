# app/main.py

from fastapi import FastAPI
from app.api.routers import main as main_router

app = FastAPI()

# Include the router from the routers directory
app.include_router(main_router.router)
