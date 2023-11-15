from pydantic import BaseModel

from app.api.core.models.Advanced import Advanced
from app.api.core.models.Traditional import Traditional


class PlayerStats(BaseModel):
    playerName: str
    gamesPlayed: int
    traditional: Traditional
    advanced: Advanced
