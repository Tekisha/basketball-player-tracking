# app/api/routers/main_routers.py

from fastapi import APIRouter
from ..endpoints import player_stats

router = APIRouter()

router.include_router(player_stats.router, prefix="/stats", tags=["stats"])
