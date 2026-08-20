from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import attendance_service


router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.get("/", response_model=list[schemas.AttendanceResponse])
def get_attendance(db: Session = Depends(get_db)):

    return attendance_service.get_attendance_records(db)


@router.get(
    "/{attendance_id}",
    response_model=schemas.AttendanceResponse
)
def get_attendance_record(
    attendance_id: int,
    db: Session = Depends(get_db)
):

    attendance = attendance_service.get_attendance_record(db, attendance_id)

    if attendance is None:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return attendance


@router.post(
    "/",
    response_model=schemas.AttendanceResponse,
    status_code=201
)
def mark_attendance(
    attendance: schemas.AttendanceCreate,
    db: Session = Depends(get_db)
):

    return attendance_service.create_attendance_record(db, attendance)


@router.put(
    "/{attendance_id}",
    response_model=schemas.AttendanceResponse
)
def update_attendance(
    attendance_id: int,
    attendance: schemas.AttendanceCreate,
    db: Session = Depends(get_db)
):

    updated_attendance = attendance_service.update_attendance_record(
        db,
        attendance_id,
        attendance
    )

    if updated_attendance is None:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return updated_attendance


@router.delete("/{attendance_id}")
def delete_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):

    deleted_attendance = attendance_service.delete_attendance_record(db, attendance_id)

    if deleted_attendance is None:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return {
        "message": "Attendance record deleted successfully"
    }