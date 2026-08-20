from sqlalchemy.orm import Session

from app import models
from app.schemas import ExaminationResultCreate


def get_examination_results(db: Session):
    return db.query(models.ExaminationResult).all()


def get_examination_result(db: Session, result_id: int):
    return (
        db.query(models.ExaminationResult)
        .filter(models.ExaminationResult.result_id == result_id)
        .first()
    )


def create_examination_result(db: Session, result: ExaminationResultCreate):

    db_result = models.ExaminationResult(
        student_id=result.student_id,
        subject_id=result.subject_id,
        marks=result.marks,
        grade=result.grade,
    )

    db.add(db_result)
    db.commit()
    db.refresh(db_result)

    return db_result


def update_examination_result(
    db: Session,
    result_id: int,
    result: ExaminationResultCreate,
):

    db_result = get_examination_result(db, result_id)

    if db_result is None:
        return None

    db_result.student_id = result.student_id
    db_result.subject_id = result.subject_id
    db_result.marks = result.marks
    db_result.grade = result.grade

    db.commit()
    db.refresh(db_result)

    return db_result


def delete_examination_result(db: Session, result_id: int):

    db_result = get_examination_result(db, result_id)

    if db_result is None:
        return None

    db.delete(db_result)
    db.commit()

    return db_result
