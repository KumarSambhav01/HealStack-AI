from backend.app.core.database import engine, Base

from backend.app.models.incident import Incident
from backend.app.models.monitoring_metric import MonitoringMetric


def init_db():

    print(Base.metadata.tables.keys())

    Base.metadata.create_all(bind=engine)