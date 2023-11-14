# app/api/endpoints/player_stats.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/player/{playerFullName}")
def get_player_info():
    return {"message": "Player information endpoint"}
