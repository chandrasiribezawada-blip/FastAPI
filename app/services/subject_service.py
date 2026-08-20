from sqlalchemy.orm import Session

from app import models
from app.schemas import SubjectCreate


def get_subjects(db: Session):
    return db.query(models.Subject).all()


def get_subject(db: Session, subject_id: int):
    return (
        db.query(models.Subject)
        .filter(models.Subject.subject_id == subject_id)
        .first()
    )


def create_subject(db: Session, subject: SubjectCreate):

    db_subject = models.Subject(
        subject_code=subject.subject_code,
        subject_name=subject.subject_name,
        credits=subject.credits,
        department_id=subject.department_id
    )

    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)

    return db_subject


def update_subject(
    db: Session,
    subject_id: int,
    subject: SubjectCreate,
):

    db_subject = get_subject(db, subject_id)

    if db_subject is None:
        return None

    db_subject.subject_code = subject.subject_code
    db_subject.subject_name = subject.subject_name
    db_subject.credits = subject.credits
    db_subject.department_id = subject.department_id

    db.commit()
    db.refresh(db_subject)

    return db_subject


def delete_subject(db: Session, subject_id: int):

    db_subject = get_subject(db, subject_id)

    if db_subject is None:
        return None

    db.delete(db_subject)
    db.commit()

    return db_subject
