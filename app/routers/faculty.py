from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import faculty_service


router = APIRouter(
    prefix="/faculty",
    tags=["Faculty"]
)


@router.get("/", response_model=list[schemas.FacultyResponse])
def get_faculty(db: Session = Depends(get_db)):

    return faculty_service.get_faculty_members(db)


@router.get(
    "/{faculty_id}",
    response_model=schemas.FacultyResponse
)
def get_faculty_member(
    faculty_id: int,
    db: Session = Depends(get_db)
):

    faculty = faculty_service.get_faculty_member(db, faculty_id)

    if faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty member not found"
        )

    return faculty


@router.post(
    "/",
    response_model=schemas.FacultyResponse,
    status_code=201
)
def create_faculty(
    faculty: schemas.FacultyCreate,
    db: Session = Depends(get_db)
):

    return faculty_service.create_faculty_member(db, faculty)


@router.put(
    "/{faculty_id}",
    response_model=schemas.FacultyResponse
)
def update_faculty(
    faculty_id: int,
    faculty: schemas.FacultyCreate,
    db: Session = Depends(get_db)
):

    updated_faculty = faculty_service.update_faculty_member(db, faculty_id, faculty)

    if updated_faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty member not found"
        )

    return updated_faculty


@router.delete("/{faculty_id}")
def delete_faculty(
    faculty_id: int,
    db: Session = Depends(get_db)
):

    deleted_faculty = faculty_service.delete_faculty_member(db, faculty_id)

    if deleted_faculty is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty member not found"
        )

    return {
        "message": "Faculty member deleted successfully"
    }