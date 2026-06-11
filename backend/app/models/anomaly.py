from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from backend.app.core.database import Base


class Anomaly(Base):

    __tablename__ = "anomalies"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    metric_type = Column(
        String,
        nullable=False
    )

    metric_value = Column(
        Float,
        nullable=False
    )

    anomaly_score = Column(
        Float,
        nullable=False
    )

    status = Column(
        String,
        default="OPEN"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )