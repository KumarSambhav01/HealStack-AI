from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.core.database import get_db

from backend.app.monitoring.metrics_collector import MetricsCollector
from backend.app.monitoring.health_checker import HealthChecker

from backend.app.services.monitoring_metric_service import (
    get_all_metrics,
    get_latest_metric,
    get_metrics_summary
)

router = APIRouter(
    prefix="/api/v1/monitoring",
    tags=["Monitoring"]
)


@router.get("/metrics")
def get_metrics():
    return MetricsCollector.collect_metrics()


@router.get("/health")
def get_health():
    metrics = MetricsCollector.collect_metrics()

    issues = HealthChecker.evaluate(metrics)

    return {
        "healthy": len(issues) == 0,
        "issues": issues
    }


@router.get("/history")
def get_monitoring_history(
    db: Session = Depends(get_db)
):
    return get_all_metrics(db)


@router.get("/latest")
def get_latest_monitoring_metric(
    db: Session = Depends(get_db)
):
    return get_latest_metric(db)


@router.get("/dashboard")
def get_dashboard_data(
    db: Session = Depends(get_db)
):
    latest_metric = get_latest_metric(db)

    summary = get_metrics_summary(db)

    return {
        "latest_metric": latest_metric,
        "summary": summary
    }