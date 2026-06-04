from fastapi import APIRouter

from backend.app.monitoring.metrics_collector import MetricsCollector

router = APIRouter(
    prefix="/api/v1/monitoring",
    tags=["Monitoring"]
)


@router.get("/metrics")
def get_metrics():
    return MetricsCollector.collect_metrics()