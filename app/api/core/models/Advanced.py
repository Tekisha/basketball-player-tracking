from pydantic import BaseModel

class Advanced(BaseModel):
    valorization: float
    effectiveFieldGoalPercentage: float
    trueShootingPercentage: float
    hollingerAssistRatio: float
