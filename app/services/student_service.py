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

    db_student = models.Student(
        student_name=student.student_name,
        email=student.email,
        mobile=student.mobile,
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

    db_student.student_name = student.student_name
    db_student.email = student.email
    db_student.mobile = student.mobile
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