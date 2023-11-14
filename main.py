# app/main_routers.py
from configparser import ConfigParser

import uvicorn
from fastapi import FastAPI, HTTPException

from app.api.core.models.PlayerStats import PlayerStats
from app.repositories.player_repository import PlayerRepository
from app.services.player_stats_service import PlayerStatsService
from app.utils.csv_parser import CsvParser


config = ConfigParser()
config.read('config.ini')

csv_file_path = config.get('App','csv_file_path')

app = FastAPI()

# Setup in-memory database and load data
game_stats_list = CsvParser.parse_csv(csv_file_path)
player_repository = PlayerRepository(game_stats_list)
player_stats_service = PlayerStatsService(player_repository)

for stat in game_stats_list:
    print(stat.player)


@app.get("/stats/player/{playerFullName}", response_model=PlayerStats)
def get_player_info(playerFullName: str):
    player_stats = player_stats_service.calculate_player_stats(playerFullName)
    print(player_stats)

    # Check if the player is found
    if player_stats is None:
        raise HTTPException(status_code=404, detail="Player not found")

    return player_stats
