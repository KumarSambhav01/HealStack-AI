import asyncio

from backend.app.monitoring.monitoring_service import MonitoringService
from backend.app.core.database import SessionLocal


class MonitoringScheduler:

    @staticmethod
    async def start():

        while True:

            db = SessionLocal()

            try:

                result = MonitoringService.run_monitoring_cycle(db)

                print(
                    f"[MONITORING] "
                    f"Incidents Created: "
                    f"{result['incidents_created']}"
                )

            except Exception as e:

                print(
                    f"[SCHEDULER ERROR] {e}"
                )

            finally:

                db.close()

            await asyncio.sleep(60)