class HealthChecker:
    """
    Evaluates system metrics and determines health status.
    """

    CPU_THRESHOLD = 90
    MEMORY_THRESHOLD = 85
    DISK_THRESHOLD = 90

    @classmethod
    def evaluate(cls, metrics: dict):
        issues = []

        if metrics["cpu_usage"] > cls.CPU_THRESHOLD:
            issues.append(
                {
                    "type": "CPU",
                    "value": metrics["cpu_usage"],
                    "severity": "HIGH",
                    "message": "CPU usage exceeded threshold"
                }
            )

        if metrics["memory_usage"] > cls.MEMORY_THRESHOLD:
            issues.append(
                {
                    "type": "MEMORY",
                    "value": metrics["memory_usage"],
                    "severity": "HIGH",
                    "message": "Memory usage exceeded threshold"
                }
            )

        if metrics["disk_usage"] > cls.DISK_THRESHOLD:
            issues.append(
                {
                    "type": "DISK",
                    "value": metrics["disk_usage"],
                    "severity": "HIGH",
                    "message": "Disk usage exceeded threshold"
                }
            )

        return issues