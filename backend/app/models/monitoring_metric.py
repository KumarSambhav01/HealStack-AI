from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from backend.app.core.database import Base


class MonitoringMetric(Base):

    __tablename__ = "monitoring_metrics"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    cpu_usage = Column(
        Float,
        nullable=False
    )

    memory_usage = Column(
        Float,
        nullable=False
    )

    disk_usage = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )