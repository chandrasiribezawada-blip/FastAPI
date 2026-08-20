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
        offering_id=attendance.offering_id,
        attendance_date=attendance.attendance_date,
        period_session=attendance.period_session,
        attendance_status=attendance.status,
        faculty_id=attendance.faculty_id,
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
    db_attendance.offering_id = attendance.offering_id
    db_attendance.attendance_date = attendance.attendance_date
    db_attendance.period_session = attendance.period_session
    db_attendance.attendance_status = attendance.status
    db_attendance.faculty_id = attendance.faculty_id

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
