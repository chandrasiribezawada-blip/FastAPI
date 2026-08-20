from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import student_activity_service


router = APIRouter(
    prefix="/student-activities",
    tags=["Student Activities"]
)


@router.get("/", response_model=list[schemas.StudentActivityResponse])
def get_student_activities(db: Session = Depends(get_db)):

    return student_activity_service.get_student_activities(db)


@router.get(
    "/{activity_id}",
    response_model=schemas.StudentActivityResponse
)
def get_student_activity(
    activity_id: int,
    db: Session = Depends(get_db)
):

    activity = student_activity_service.get_student_activity(db, activity_id)

    if activity is None:
        raise HTTPException(
            status_code=404,
            detail="Student activity not found"
        )

    return activity


@router.post(
    "/",
    response_model=schemas.StudentActivityResponse,
    status_code=201
)
def create_student_activity(
    activity: schemas.StudentActivityCreate,
    db: Session = Depends(get_db)
):

    return student_activity_service.create_student_activity(db, activity)


@router.put(
    "/{activity_id}",
    response_model=schemas.StudentActivityResponse
)
def update_student_activity(
    activity_id: int,
    activity: schemas.StudentActivityCreate,
    db: Session = Depends(get_db)
):

    updated_activity = student_activity_service.update_student_activity(
        db,
        activity_id,
        activity
    )

    if updated_activity is None:
        raise HTTPException(
            status_code=404,
            detail="Student activity not found"
        )

    return updated_activity


@router.delete("/{activity_id}")
def delete_student_activity(
    activity_id: int,
    db: Session = Depends(get_db)
):

    deleted_activity = student_activity_service.delete_student_activity(
        db,
        activity_id
    )

    if deleted_activity is None:
        raise HTTPException(
            status_code=404,
            detail="Student activity not found"
        )

    return {
        "message": "Student activity deleted successfully"
    }