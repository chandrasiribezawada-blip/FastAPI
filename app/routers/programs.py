from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import program_service


router = APIRouter(
    prefix="/programs",
    tags=["Programs"]
)


@router.get("/", response_model=list[schemas.ProgramResponse])
def get_programs(db: Session = Depends(get_db)):

    return program_service.get_programs(db)


@router.get(
    "/{program_id}",
    response_model=schemas.ProgramResponse
)
def get_program(
    program_id: int,
    db: Session = Depends(get_db)
):

    program = program_service.get_program(db, program_id)

    if program is None:
        raise HTTPException(
            status_code=404,
            detail="Program not found"
        )

    return program


@router.post(
    "/",
    response_model=schemas.ProgramResponse,
    status_code=201
)
def create_program(
    program: schemas.ProgramCreate,
    db: Session = Depends(get_db)
):

    return program_service.create_program(db, program)


@router.put(
    "/{program_id}",
    response_model=schemas.ProgramResponse
)
def update_program(
    program_id: int,
    program: schemas.ProgramCreate,
    db: Session = Depends(get_db)
):

    updated_program = program_service.update_program(db, program_id, program)

    if updated_program is None:
        raise HTTPException(
            status_code=404,
            detail="Program not found"
        )

    return updated_program


@router.delete("/{program_id}")
def delete_program(
    program_id: int,
    db: Session = Depends(get_db)
):

    deleted_program = program_service.delete_program(db, program_id)

    if deleted_program is None:
        raise HTTPException(
            status_code=404,
            detail="Program not found"
        )

    return {
        "message": "Program deleted successfully"
    }