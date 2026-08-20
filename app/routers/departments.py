from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import department_service


router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.get("/", response_model=list[schemas.DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):

    return department_service.get_departments(db)


@router.get(
    "/{department_id}",
    response_model=schemas.DepartmentResponse
)
def get_department(
    department_id: int,
    db: Session = Depends(get_db)
):

    department = department_service.get_department(db, department_id)

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return department


@router.post(
    "/",
    response_model=schemas.DepartmentResponse,
    status_code=201
)
def create_department(
    department: schemas.DepartmentCreate,
    db: Session = Depends(get_db)
):

    return department_service.create_department(db, department)


@router.put(
    "/{department_id}",
    response_model=schemas.DepartmentResponse
)
def update_department(
    department_id: int,
    department: schemas.DepartmentCreate,
    db: Session = Depends(get_db)
):

    updated_department = department_service.update_department(db, department_id, department)

    if updated_department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return updated_department


@router.delete("/{department_id}")
def delete_department(
    department_id: int,
    db: Session = Depends(get_db)
):

    deleted_department = department_service.delete_department(db, department_id)

    if deleted_department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return {
        "message": "Department deleted successfully"
    }