from sqlalchemy.orm import Session

from backend.app.models.anomaly import Anomaly


def create_anomaly(
    db: Session,
    metric_type: str,
    metric_value: float,
    anomaly_score: float,
    status: str
):
    anomaly = Anomaly(
        metric_type=metric_type,
        metric_value=float(metric_value),
        anomaly_score=float(anomaly_score),
        status=status
    )

    db.add(anomaly)

    db.commit()

    db.refresh(anomaly)

    return anomaly


def get_all_anomalies(db: Session):
    return (
        db.query(Anomaly)
        .order_by(Anomaly.created_at.desc())
        .all()
    )


def get_latest_anomaly(db: Session):
    return (
        db.query(Anomaly)
        .order_by(Anomaly.created_at.desc())
        .first()
    )