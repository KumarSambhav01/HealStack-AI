from pydantic import BaseModel
from datetime import datetime


class AnomalyResponse(BaseModel):
    id: int
    metric_type: str
    metric_value: float
    anomaly_score: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True