from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import student_service


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get(
    "/",
    response_model=list[schemas.StudentResponse],
    summary="List all students"
)
def get_students(db: Session = Depends(get_db)):

    return student_service.get_students(db)


@router.get(
    "/{student_id}",
    response_model=schemas.StudentResponse,
    summary="Get a student by ID"
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = student_service.get_student(
        db,
        student_id
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.post(
    "/",
    response_model=schemas.StudentResponse,
    status_code=201,
    summary="Create a student"
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):

    return student_service.create_student(
        db,
        student
    )


@router.put(
    "/{student_id}",
    response_model=schemas.StudentResponse,
    summary="Update a student by ID"
)
def update_student(
    student_id: int,
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):

    updated_student = student_service.update_student(
        db,
        student_id,
        student
    )

    if updated_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student


@router.delete(
    "/{student_id}",
    summary="Delete a student by ID"
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    deleted_student = student_service.delete_student(
        db,
        student_id
    )

    if deleted_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }