from pydantic import BaseModel


class TwoPoints(BaseModel):
    attempts: float
    made: float
    shootingPercentage: float

