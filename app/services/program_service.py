from sqlalchemy.orm import Session

from app import models
from app.schemas import ProgramCreate


def get_programs(db: Session):
    return db.query(models.Program).all()


def get_program(db: Session, program_id: int):
    return (
        db.query(models.Program)
        .filter(models.Program.program_id == program_id)
        .first()
    )


def create_program(db: Session, program: ProgramCreate):

    db_program = models.Program(
        program_code=program.program_code,
        program_name=program.program_name,
        department_id=program.department_id,
    )

    db.add(db_program)
    db.commit()
    db.refresh(db_program)

    return db_program


def update_program(
    db: Session,
    program_id: int,
    program: ProgramCreate,
):

    db_program = get_program(db, program_id)

    if db_program is None:
        return None

    db_program.program_code = program.program_code
    db_program.program_name = program.program_name
    db_program.department_id = program.department_id

    db.commit()
    db.refresh(db_program)

    return db_program


def delete_program(db: Session, program_id: int):

    db_program = get_program(db, program_id)

    if db_program is None:
        return None

    db.delete(db_program)
    db.commit()

    return db_program
