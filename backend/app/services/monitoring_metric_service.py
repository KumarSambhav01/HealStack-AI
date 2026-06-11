from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.app.models.monitoring_metric import MonitoringMetric


def create_monitoring_metric(
    db: Session,
    metrics: dict
):
    try:
        metric = MonitoringMetric(
            cpu_usage=metrics["cpu_usage"],
            memory_usage=metrics["memory_usage"],
            disk_usage=metrics["disk_usage"]
        )

        db.add(metric)

        db.commit()

        db.refresh(metric)

        print(
            f"[METRICS SAVED] "
            f"ID={metric.id} "
            f"CPU={metric.cpu_usage} "
            f"MEM={metric.memory_usage} "
            f"DISK={metric.disk_usage}"
        )

        return metric

    except Exception:
        db.rollback()
        raise


def get_all_metrics(db: Session):
    return (
        db.query(MonitoringMetric)
        .order_by(MonitoringMetric.created_at.desc())
        .all()
    )


def get_latest_metric(db: Session):
    return (
        db.query(MonitoringMetric)
        .order_by(MonitoringMetric.created_at.desc())
        .first()
    )


def get_metrics_summary(db: Session):

    total_records = (
        db.query(MonitoringMetric)
        .count()
    )

    avg_cpu = (
        db.query(func.avg(MonitoringMetric.cpu_usage))
        .scalar()
    )

    avg_memory = (
        db.query(func.avg(MonitoringMetric.memory_usage))
        .scalar()
    )

    avg_disk = (
        db.query(func.avg(MonitoringMetric.disk_usage))
        .scalar()
    )

    return {
        "total_records": total_records,
        "avg_cpu": round(avg_cpu or 0, 2),
        "avg_memory": round(avg_memory or 0, 2),
        "avg_disk": round(avg_disk or 0, 2)
    }