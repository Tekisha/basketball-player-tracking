from pydantic import BaseModel


class ThreePoints(BaseModel):
    attempts: float
    made: float
    shootingPercentage: float
