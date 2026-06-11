from pydantic import BaseModel
from datetime import datetime


class MonitoringMetricResponse(BaseModel):
    id: int
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    created_at: datetime

    class Config:
        from_attributes = True