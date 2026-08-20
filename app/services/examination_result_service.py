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
        offering_id=result.offering_id,
        internal_marks=result.internal_marks,
        external_marks=result.external_marks,
        total_marks=result.total_marks,
        grade=result.grade,
        result_status=result.result_status,
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
    db_result.offering_id = result.offering_id
    db_result.internal_marks = result.internal_marks
    db_result.external_marks = result.external_marks
    db_result.total_marks = result.total_marks
    db_result.grade = result.grade
    db_result.result_status = result.result_status

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
