from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.core.database import get_db

from backend.app.services.anomaly_service import (
    get_all_anomalies,
    get_latest_anomaly
)

from backend.app.services.anomaly_detection_service import (
    run_anomaly_detection
)

router = APIRouter(
    prefix="/api/v1/anomalies",
    tags=["Anomalies"]
)


@router.get("/")
def get_anomalies(
    db: Session = Depends(get_db)
):
    return get_all_anomalies(db)


@router.get("/latest")
def get_latest(
    db: Session = Depends(get_db)
):
    return get_latest_anomaly(db)


@router.post("/run")
def run_detection(
    db: Session = Depends(get_db)
):
    return run_anomaly_detection(db)