from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import faculty_assignment_service


router = APIRouter(
    prefix="/faculty-assignments",
    tags=["Faculty Assignments"]
)


@router.get("/", response_model=list[schemas.FacultyAssignmentResponse])
def get_faculty_assignments(db: Session = Depends(get_db)):

    return faculty_assignment_service.get_faculty_assignments(db)


@router.get(
    "/{assignment_id}",
    response_model=schemas.FacultyAssignmentResponse
)
def get_faculty_assignment(
    assignment_id: int,
    db: Session = Depends(get_db)
):

    assignment = faculty_assignment_service.get_faculty_assignment(db, assignment_id)

    if assignment is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty assignment not found"
        )

    return assignment


@router.post(
    "/",
    response_model=schemas.FacultyAssignmentResponse,
    status_code=201
)
def create_faculty_assignment(
    assignment: schemas.FacultyAssignmentCreate,
    db: Session = Depends(get_db)
):

    return faculty_assignment_service.create_faculty_assignment(db, assignment)


@router.put(
    "/{assignment_id}",
    response_model=schemas.FacultyAssignmentResponse
)
def update_faculty_assignment(
    assignment_id: int,
    assignment: schemas.FacultyAssignmentCreate,
    db: Session = Depends(get_db)
):

    updated_assignment = faculty_assignment_service.update_faculty_assignment(
        db,
        assignment_id,
        assignment
    )

    if updated_assignment is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty assignment not found"
        )

    return updated_assignment


@router.delete("/{assignment_id}")
def delete_faculty_assignment(
    assignment_id: int,
    db: Session = Depends(get_db)
):

    deleted_assignment = faculty_assignment_service.delete_faculty_assignment(
        db,
        assignment_id
    )

    if deleted_assignment is None:
        raise HTTPException(
            status_code=404,
            detail="Faculty assignment not found"
        )

    return {
        "message": "Faculty assignment deleted successfully"
    }