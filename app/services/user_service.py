from sqlalchemy.orm import Session

from app import models
from app.schemas import UserCreate


def get_users(db: Session):
    return db.query(models.User).all()


def get_user(db: Session, user_id: int):
    return (
        db.query(models.User)
        .filter(models.User.user_id == user_id)
        .first()
    )


def create_user(db: Session, user: UserCreate):

    db_user = models.User(
        username=user.username,
        password_hash=user.password,
        role=user.role,
        is_active=user.is_active,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(
    db: Session,
    user_id: int,
    user: UserCreate,
):

    db_user = get_user(db, user_id)

    if db_user is None:
        return None

    db_user.username = user.username
    db_user.password_hash = user.password
    db_user.role = user.role
    db_user.is_active = user.is_active

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):

    db_user = get_user(db, user_id)

    if db_user is None:
        return None

    db.delete(db_user)
    db.commit()

    return db_user
