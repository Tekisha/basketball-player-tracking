# app/api/routers/main.py

from fastapi import APIRouter
from ..endpoints import player_stats

router = APIRouter()

router.include_router(player_stats.router, prefix="/stats", tags=["stats"])
