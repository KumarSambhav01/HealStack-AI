import psutil
from datetime import datetime


class MetricsCollector:
    """
    Collects system metrics from the host machine.
    """

    @staticmethod
    def collect_metrics():
        return {
            "cpu_usage": psutil.cpu_percent(interval=1),
            "memory_usage": psutil.virtual_memory().percent,
            "disk_usage": psutil.disk_usage("/").percent,
            "timestamp": datetime.utcnow().isoformat()
        }