from backend.app.core.database import SessionLocal

from backend.app.monitoring.monitoring_service import (
    MonitoringService
)


db = SessionLocal()

try:
    result = MonitoringService.run_monitoring_cycle(db)

    print("Monitoring Result:")
    print(result)

finally:
    db.close()