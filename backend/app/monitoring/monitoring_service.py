from sqlalchemy.orm import Session

from backend.app.monitoring.metrics_collector import MetricsCollector
from backend.app.monitoring.health_checker import HealthChecker
from backend.app.monitoring.incident_generator import IncidentGenerator

from backend.app.schemas.incident import IncidentCreate
from backend.app.services.incident_service import create_incident


class MonitoringService:
    """
    Main orchestration service for monitoring.
    """

    @staticmethod
    def run_monitoring_cycle(db: Session):
        # Step 1: Collect metrics
        metrics = MetricsCollector.collect_metrics()

        # Step 2: Evaluate health
        issues = HealthChecker.evaluate(metrics)

        # Step 3: Generate incident payloads
        incidents = IncidentGenerator.generate_incidents(issues)

        created_incidents = []

        # Step 4: Store incidents in database
        for incident_data in incidents:

            incident_schema = IncidentCreate(
                title=incident_data["title"],
                description=incident_data["description"],
                severity=incident_data["severity"]
            )

            created_incident = create_incident(
                db=db,
                incident=incident_schema
            )

            created_incidents.append(created_incident)

        return {
            "metrics": metrics,
            "issues": issues,
            "incidents_created": len(created_incidents)
        }