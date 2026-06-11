from sqlalchemy.orm import Session

from backend.app.models.monitoring_metric import MonitoringMetric

from backend.app.ai_engine.anomaly_detector import (
    AnomalyDetector
)

from backend.app.services.anomaly_service import (
    create_anomaly
)


def run_anomaly_detection(
    db: Session
):

    metrics = (
        db.query(MonitoringMetric)
        .order_by(MonitoringMetric.created_at.asc())
        .all()
    )

    if len(metrics) < 10:
        print(
            "[ANOMALY DETECTOR] "
            "Not enough data"
        )
        return []

    dataset = []

    for metric in metrics:

        dataset.append({
            "cpu_usage": float(metric.cpu_usage),
            "memory_usage": float(metric.memory_usage),
            "disk_usage": float(metric.disk_usage)
        })

    anomalies = AnomalyDetector.detect(
        dataset
    )

    saved = []

    for anomaly in anomalies:

        record = create_anomaly(
            db=db,
            metric_type="system_metrics",
            metric_value=float(
                anomaly["cpu_usage"]
            ),
            anomaly_score=float(1.0),
            status="detected"
        )

        saved.append(record)

    print(
        f"[ANOMALY DETECTOR] "
        f"{len(saved)} anomalies saved"
    )

    return saved