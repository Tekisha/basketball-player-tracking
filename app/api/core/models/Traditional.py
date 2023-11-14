from pydantic import BaseModel

from app.api.core.models.FreeThrows import FreeThrows
from app.api.core.models.ThreePoints import ThreePoints
from app.api.core.models.TwoPoints import TwoPoints


class Traditional(BaseModel):
    freeThrows: FreeThrows
    twoPoints: TwoPoints
    threePoints: ThreePoints
    points: float
    rebounds: float
    blocks: float
    assists: float
    steals: float
    turnovers: float
