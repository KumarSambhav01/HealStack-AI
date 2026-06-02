from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.schemas.incident import (
    IncidentCreate,
    IncidentUpdate,
    IncidentResponse
)
from backend.app.services.incident_service import (
    create_incident,
    get_incidents,
    get_incident_by_id,
    update_incident,
    delete_incident
)

router = APIRouter(
    prefix="/api/v1/incidents",
    tags=["Incidents"]
)


@router.post(
    "/",
    response_model=IncidentResponse
)
def create_incident_endpoint(
    incident: IncidentCreate,
    db: Session = Depends(get_db)
):
    return create_incident(db, incident)


@router.get(
    "/",
    response_model=List[IncidentResponse]
)
def get_all_incidents(
    db: Session = Depends(get_db)
):
    return get_incidents(db)


@router.get(
    "/{incident_id}",
    response_model=IncidentResponse
)
def get_incident(
    incident_id: int,
    db: Session = Depends(get_db)
):
    incident = get_incident_by_id(
        db,
        incident_id
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return incident


@router.put(
    "/{incident_id}",
    response_model=IncidentResponse
)
def update_incident_endpoint(
    incident_id: int,
    incident_data: IncidentUpdate,
    db: Session = Depends(get_db)
):
    incident = update_incident(
        db,
        incident_id,
        incident_data
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return incident


@router.delete(
    "/{incident_id}"
)
def delete_incident_endpoint(
    incident_id: int,
    db: Session = Depends(get_db)
):
    success = delete_incident(
        db,
        incident_id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return {
        "message": "Incident deleted successfully"
    }   