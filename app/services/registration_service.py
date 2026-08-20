from sqlalchemy.orm import Session

from app import models
from app.schemas import RegistrationCreate


def get_registrations(db: Session):
    return db.query(models.Registration).all()


def get_registration(db: Session, registration_id: int):
    return (
        db.query(models.Registration)
        .filter(models.Registration.registration_id == registration_id)
        .first()
    )


def create_registration(db: Session, registration: RegistrationCreate):

    db_registration = models.Registration(
        student_id=registration.student_id,
        offering_id=registration.offering_id,
        registration_date=registration.registration_date,
        registration_status=registration.status,
    )

    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)

    return db_registration


def update_registration(
    db: Session,
    registration_id: int,
    registration: RegistrationCreate,
):

    db_registration = get_registration(db, registration_id)

    if db_registration is None:
        return None

    db_registration.student_id = registration.student_id
    db_registration.offering_id = registration.offering_id
    db_registration.registration_date = registration.registration_date
    db_registration.registration_status = registration.status

    db.commit()
    db.refresh(db_registration)

    return db_registration


def delete_registration(db: Session, registration_id: int):

    db_registration = get_registration(db, registration_id)

    if db_registration is None:
        return None

    db.delete(db_registration)
    db.commit()

    return db_registration
