from backend.app.monitoring.metrics_collector import MetricsCollector
from backend.app.monitoring.health_checker import HealthChecker
from backend.app.monitoring.incident_generator import IncidentGenerator

metrics = MetricsCollector.collect_metrics()

issues = HealthChecker.evaluate(metrics)

incidents = IncidentGenerator.generate_incidents(issues)

print("Metrics:")
print(metrics)

print("\nIssues:")
print(issues)

print("\nIncidents:")
print(incidents)