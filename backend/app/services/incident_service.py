from sqlalchemy.orm import Session

from backend.app.models.incident import Incident
from backend.app.schemas.incident import (
    IncidentCreate,
    IncidentUpdate
)


def create_incident(
    db: Session,
    incident: IncidentCreate
):
    db_incident = Incident(
        title=incident.title,
        description=incident.description,
        severity=incident.severity
    )

    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)

    return db_incident


def get_incidents(
    db: Session
):
    return db.query(Incident).all()


def get_incident_by_id(
    db: Session,
    incident_id: int
):
    return (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )


def update_incident(
    db: Session,
    incident_id: int,
    incident_data: IncidentUpdate
):
    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if not incident:
        return None

    update_data = incident_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(incident, key, value)

    db.commit()
    db.refresh(incident)

    return incident


def delete_incident(
    db: Session,
    incident_id: int
):
    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if not incident:
        return False

    db.delete(incident)
    db.commit()

    return True
