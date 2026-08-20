from sqlalchemy.orm import Session

from app import models
from app.schemas import AttendanceCreate


def get_attendance_records(db: Session):
    return db.query(models.Attendance).all()


def get_attendance_record(db: Session, attendance_id: int):
    return (
        db.query(models.Attendance)
        .filter(models.Attendance.attendance_id == attendance_id)
        .first()
    )


def create_attendance_record(db: Session, attendance: AttendanceCreate):

    db_attendance = models.Attendance(
        student_id=attendance.student_id,
        subject_id=attendance.subject_id,
        attendance_date=attendance.attendance_date,
        status=attendance.status,
    )

    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)

    return db_attendance


def update_attendance_record(
    db: Session,
    attendance_id: int,
    attendance: AttendanceCreate,
):

    db_attendance = get_attendance_record(db, attendance_id)

    if db_attendance is None:
        return None

    db_attendance.student_id = attendance.student_id
    db_attendance.subject_id = attendance.subject_id
    db_attendance.attendance_date = attendance.attendance_date
    db_attendance.status = attendance.status

    db.commit()
    db.refresh(db_attendance)

    return db_attendance


def delete_attendance_record(db: Session, attendance_id: int):

    db_attendance = get_attendance_record(db, attendance_id)

    if db_attendance is None:
        return None

    db.delete(db_attendance)
    db.commit()

    return db_attendance
