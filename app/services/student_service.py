from sqlalchemy.orm import Session

from app import models
from app.schemas import StudentCreate


def get_students(db: Session):
    return db.query(models.Student).all()


def get_student(db: Session, student_id: int):
    return (
        db.query(models.Student)
        .filter(models.Student.student_id == student_id)
        .first()
    )


def create_student(db: Session, student: StudentCreate):

    name_parts = student.student_name.split(maxsplit=1)

    db_student = models.Student(
        roll_number=student.roll_number,
        first_name=name_parts[0],
        last_name=name_parts[1] if len(name_parts) > 1 else None,
        email=student.email,
        mobile=student.mobile,
        admission_year=student.admission_year,
        department_id=student.department_id,
        program_id=student.program_id
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def update_student(
    db: Session,
    student_id: int,
    student: StudentCreate
):

    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    name_parts = student.student_name.split(maxsplit=1)
    db_student.roll_number = student.roll_number
    db_student.first_name = name_parts[0]
    db_student.last_name = name_parts[1] if len(name_parts) > 1 else None
    db_student.email = student.email
    db_student.mobile = student.mobile
    db_student.admission_year = student.admission_year
    db_student.department_id = student.department_id
    db_student.program_id = student.program_id

    db.commit()
    db.refresh(db_student)

    return db_student


def delete_student(db: Session, student_id: int):

    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    db.delete(db_student)
    db.commit()

    return db_student