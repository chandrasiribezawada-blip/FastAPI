from sqlalchemy.orm import Session

from app import models
from app.schemas import FacultyAssignmentCreate


def get_faculty_assignments(db: Session):
    return db.query(models.FacultyAssignment).all()


def get_faculty_assignment(db: Session, assignment_id: int):
    return (
        db.query(models.FacultyAssignment)
        .filter(models.FacultyAssignment.assignment_id == assignment_id)
        .first()
    )


def create_faculty_assignment(db: Session, assignment: FacultyAssignmentCreate):

    db_assignment = models.FacultyAssignment(
        faculty_id=assignment.faculty_id,
        offering_id=assignment.offering_id,
        role=assignment.role,
    )

    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)

    return db_assignment


def update_faculty_assignment(
    db: Session,
    assignment_id: int,
    assignment: FacultyAssignmentCreate,
):

    db_assignment = get_faculty_assignment(db, assignment_id)

    if db_assignment is None:
        return None

    db_assignment.faculty_id = assignment.faculty_id
    db_assignment.offering_id = assignment.offering_id
    db_assignment.role = assignment.role

    db.commit()
    db.refresh(db_assignment)

    return db_assignment


def delete_faculty_assignment(db: Session, assignment_id: int):

    db_assignment = get_faculty_assignment(db, assignment_id)

    if db_assignment is None:
        return None

    db.delete(db_assignment)
    db.commit()

    return db_assignment
