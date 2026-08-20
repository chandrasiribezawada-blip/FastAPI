from sqlalchemy.orm import Session

from app import models
from app.schemas import FacultyCreate


def get_faculty_members(db: Session):
    return db.query(models.Faculty).all()


def get_faculty_member(db: Session, faculty_id: int):
    return (
        db.query(models.Faculty)
        .filter(models.Faculty.faculty_id == faculty_id)
        .first()
    )


def create_faculty_member(db: Session, faculty: FacultyCreate):

    name_parts = faculty.faculty_name.split(maxsplit=1)

    db_faculty = models.Faculty(
        employee_id=faculty.employee_id,
        first_name=name_parts[0],
        last_name=name_parts[1] if len(name_parts) > 1 else None,
        email=faculty.email,
        mobile=faculty.mobile,
        department_id=faculty.department_id,
    )

    db.add(db_faculty)
    db.commit()
    db.refresh(db_faculty)

    return db_faculty


def update_faculty_member(
    db: Session,
    faculty_id: int,
    faculty: FacultyCreate,
):

    db_faculty = get_faculty_member(db, faculty_id)

    if db_faculty is None:
        return None

    name_parts = faculty.faculty_name.split(maxsplit=1)
    db_faculty.employee_id = faculty.employee_id
    db_faculty.first_name = name_parts[0]
    db_faculty.last_name = name_parts[1] if len(name_parts) > 1 else None
    db_faculty.email = faculty.email
    db_faculty.mobile = faculty.mobile
    db_faculty.department_id = faculty.department_id

    db.commit()
    db.refresh(db_faculty)

    return db_faculty


def delete_faculty_member(db: Session, faculty_id: int):

    db_faculty = get_faculty_member(db, faculty_id)

    if db_faculty is None:
        return None

    db.delete(db_faculty)
    db.commit()

    return db_faculty
