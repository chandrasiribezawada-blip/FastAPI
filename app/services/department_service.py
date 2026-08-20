from sqlalchemy.orm import Session

from app import models
from app.schemas import DepartmentCreate


def get_departments(db: Session):
    return db.query(models.Department).all()


def get_department(db: Session, department_id: int):
    return (
        db.query(models.Department)
        .filter(models.Department.department_id == department_id)
        .first()
    )


def create_department(db: Session, department: DepartmentCreate):

    db_department = models.Department(
        department_code=department.department_code,
        department_name=department.department_name,
        hod_faculty_id=department.hod_faculty_id,
        contact_email=department.contact_email,
        contact_mobile=department.contact_mobile,
    )

    db.add(db_department)
    db.commit()
    db.refresh(db_department)

    return db_department


def update_department(
    db: Session,
    department_id: int,
    department: DepartmentCreate,
):

    db_department = get_department(db, department_id)

    if db_department is None:
        return None

    db_department.department_code = department.department_code
    db_department.department_name = department.department_name
    db_department.hod_faculty_id = department.hod_faculty_id
    db_department.contact_email = department.contact_email
    db_department.contact_mobile = department.contact_mobile

    db.commit()
    db.refresh(db_department)

    return db_department


def delete_department(db: Session, department_id: int):

    db_department = get_department(db, department_id)

    if db_department is None:
        return None

    db.delete(db_department)
    db.commit()

    return db_department
