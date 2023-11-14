# app/api/endpoints/player_stats.py

from fastapi import APIRouter, HTTPException

from app.api.core.models.PlayerStats import PlayerStats

router = APIRouter()


@router.get("/player/{playerFullName}", response_model=PlayerStats)
def get_player_info(playerFullName: str):
    player_data = {
        "playerName": playerFullName,
        "gamesPlayed": 10,
        "traditional": {
            "freeThrows": {"attempts": 13.7, "made": 8.3, "shootingPercentage": 66.3},
            "twoPoints": {"attempts": 20.5, "made": 12.8, "shootingPercentage": 62.4},
            "threePoints": {"attempts": 7.2, "made": 3.5, "shootingPercentage": 48.6},
            "points": 24.4,
            "rebounds": 12.1,
            "blocks": 4.3,
            "assists": 9.7,
            "steals": 3.1,
            "turnovers": 5,
        },
        "advanced": {
            "valorization": 50.6,
            "effectiveFieldGoalPercentage": 55.2,
            "trueShootingPercentage": 58.7,
            "hollingerAssistRatio": 30.5,
        }
    }

    # Check if the player is found
    if playerFullName.lower() != "john doe":
        raise HTTPException(status_code=404, detail="Player not found")

    return PlayerStats(**player_data)
