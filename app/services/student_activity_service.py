from sqlalchemy.orm import Session

from app import models
from app.schemas import StudentActivityCreate


def get_student_activities(db: Session):
    return db.query(models.StudentActivity).all()


def get_student_activity(db: Session, activity_id: int):
    return (
        db.query(models.StudentActivity)
        .filter(models.StudentActivity.activity_id == activity_id)
        .first()
    )


def create_student_activity(db: Session, activity: StudentActivityCreate):

    db_activity = models.StudentActivity(
        student_id=activity.student_id,
        activity_name=activity.activity_name,
        description=activity.description,
        activity_date=activity.activity_date,
    )

    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)

    return db_activity


def update_student_activity(
    db: Session,
    activity_id: int,
    activity: StudentActivityCreate,
):

    db_activity = get_student_activity(db, activity_id)

    if db_activity is None:
        return None

    db_activity.student_id = activity.student_id
    db_activity.activity_name = activity.activity_name
    db_activity.description = activity.description
    db_activity.activity_date = activity.activity_date

    db.commit()
    db.refresh(db_activity)

    return db_activity


def delete_student_activity(db: Session, activity_id: int):

    db_activity = get_student_activity(db, activity_id)

    if db_activity is None:
        return None

    db.delete(db_activity)
    db.commit()

    return db_activity
