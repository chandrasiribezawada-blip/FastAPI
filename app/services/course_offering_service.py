from sqlalchemy.orm import Session

from app import models
from app.schemas import CourseOfferingCreate


def get_course_offerings(db: Session):
    return db.query(models.CourseOffering).all()


def get_course_offering(db: Session, offering_id: int):
    return (
        db.query(models.CourseOffering)
        .filter(models.CourseOffering.offering_id == offering_id)
        .first()
    )


def create_course_offering(db: Session, offering: CourseOfferingCreate):

    db_offering = models.CourseOffering(
        subject_id=offering.subject_id,
        faculty_id=offering.faculty_id,
        semester=offering.semester,
        academic_year=offering.academic_year,
    )

    db.add(db_offering)
    db.commit()
    db.refresh(db_offering)

    return db_offering


def update_course_offering(
    db: Session,
    offering_id: int,
    offering: CourseOfferingCreate,
):

    db_offering = get_course_offering(db, offering_id)

    if db_offering is None:
        return None

    db_offering.subject_id = offering.subject_id
    db_offering.faculty_id = offering.faculty_id
    db_offering.semester = offering.semester
    db_offering.academic_year = offering.academic_year

    db.commit()
    db.refresh(db_offering)

    return db_offering


def delete_course_offering(db: Session, offering_id: int):

    db_offering = get_course_offering(db, offering_id)

    if db_offering is None:
        return None

    db.delete(db_offering)
    db.commit()

    return db_offering
