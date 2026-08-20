from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import subject_service


router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"]
)


@router.get("/", response_model=list[schemas.SubjectResponse])
def get_subjects(db: Session = Depends(get_db)):

    return subject_service.get_subjects(db)


@router.get(
    "/{subject_id}",
    response_model=schemas.SubjectResponse
)
def get_subject(
    subject_id: int,
    db: Session = Depends(get_db)
):

    subject = subject_service.get_subject(db, subject_id)

    if subject is None:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    return subject


@router.post(
    "/",
    response_model=schemas.SubjectResponse,
    status_code=201
)
def create_subject(
    subject: schemas.SubjectCreate,
    db: Session = Depends(get_db)
):

    return subject_service.create_subject(db, subject)


@router.put(
    "/{subject_id}",
    response_model=schemas.SubjectResponse
)
def update_subject(
    subject_id: int,
    subject: schemas.SubjectCreate,
    db: Session = Depends(get_db)
):

    updated_subject = subject_service.update_subject(db, subject_id, subject)

    if updated_subject is None:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    return updated_subject


@router.delete("/{subject_id}")
def delete_subject(
    subject_id: int,
    db: Session = Depends(get_db)
):

    deleted_subject = subject_service.delete_subject(db, subject_id)

    if deleted_subject is None:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    return {
        "message": "Subject deleted successfully"
    }