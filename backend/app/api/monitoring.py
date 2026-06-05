from fastapi import APIRouter

from backend.app.monitoring.metrics_collector import MetricsCollector
from backend.app.monitoring.health_checker import HealthChecker 
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