from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import course_offering_service


router = APIRouter(
    prefix="/course-offerings",
    tags=["Courses"]
)


@router.get("/", response_model=list[schemas.CourseOfferingResponse])
def get_course_offerings(db: Session = Depends(get_db)):

    return course_offering_service.get_course_offerings(db)


@router.get(
    "/{offering_id}",
    response_model=schemas.CourseOfferingResponse
)
def get_course_offering(
    offering_id: int,
    db: Session = Depends(get_db)
):

    offering = course_offering_service.get_course_offering(db, offering_id)

    if offering is None:
        raise HTTPException(
            status_code=404,
            detail="Course offering not found"
        )

    return offering


@router.post(
    "/",
    response_model=schemas.CourseOfferingResponse,
    status_code=201
)
def create_course_offering(
    offering: schemas.CourseOfferingCreate,
    db: Session = Depends(get_db)
):

    return course_offering_service.create_course_offering(db, offering)


@router.put(
    "/{offering_id}",
    response_model=schemas.CourseOfferingResponse
)
def update_course_offering(
    offering_id: int,
    offering: schemas.CourseOfferingCreate,
    db: Session = Depends(get_db)
):

    updated_offering = course_offering_service.update_course_offering(
        db,
        offering_id,
        offering
    )

    if updated_offering is None:
        raise HTTPException(
            status_code=404,
            detail="Course offering not found"
        )

    return updated_offering


@router.delete("/{offering_id}")
def delete_course_offering(
    offering_id: int,
    db: Session = Depends(get_db)
):

    deleted_offering = course_offering_service.delete_course_offering(db, offering_id)

    if deleted_offering is None:
        raise HTTPException(
            status_code=404,
            detail="Course offering not found"
        )

    return {
        "message": "Course offering deleted successfully"
    }