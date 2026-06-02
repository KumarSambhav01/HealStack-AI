class IncidentGenerator:
    """
    Converts monitoring issues into incident payloads.
    """

    @staticmethod
    def generate_incidents(issues: list):
        incidents = []

        for issue in issues:
            incidents.append(
                {
                    "title": f"{issue['type']} Usage Critical",
                    "description": (
                        f"{issue['message']}. "
                        f"Current value: {issue['value']}%"
                    ),
                    "severity": issue["severity"]
                }
            )

        return incidents