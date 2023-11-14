from pydantic import BaseModel


class FreeThrows(BaseModel):
    attempts: float
    made: float
    shootingPercentage: float