from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import registration_service


router = APIRouter(
    prefix="/registrations",
    tags=["Registrations"]
)


@router.get("/", response_model=list[schemas.RegistrationResponse])
def get_registrations(db: Session = Depends(get_db)):

    return registration_service.get_registrations(db)


@router.get(
    "/{registration_id}",
    response_model=schemas.RegistrationResponse
)
def get_registration(
    registration_id: int,
    db: Session = Depends(get_db)
):

    registration = registration_service.get_registration(db, registration_id)

    if registration is None:
        raise HTTPException(
            status_code=404,
            detail="Registration not found"
        )

    return registration


@router.post(
    "/",
    response_model=schemas.RegistrationResponse,
    status_code=201
)
def create_registration(
    registration: schemas.RegistrationCreate,
    db: Session = Depends(get_db)
):

    return registration_service.create_registration(db, registration)


@router.put(
    "/{registration_id}",
    response_model=schemas.RegistrationResponse
)
def update_registration(
    registration_id: int,
    registration: schemas.RegistrationCreate,
    db: Session = Depends(get_db)
):

    updated_registration = registration_service.update_registration(
        db,
        registration_id,
        registration
    )

    if updated_registration is None:
        raise HTTPException(
            status_code=404,
            detail="Registration not found"
        )

    return updated_registration


@router.delete("/{registration_id}")
def delete_registration(
    registration_id: int,
    db: Session = Depends(get_db)
):

    deleted_registration = registration_service.delete_registration(db, registration_id)

    if deleted_registration is None:
        raise HTTPException(
            status_code=404,
            detail="Registration not found"
        )

    return {
        "message": "Registration deleted successfully"
    }