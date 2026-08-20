from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import examination_result_service


router = APIRouter(
    prefix="/examination-results",
    tags=["Examination Results"]
)


@router.get("/", response_model=list[schemas.ExaminationResultResponse])
def get_examination_results(db: Session = Depends(get_db)):

    return examination_result_service.get_examination_results(db)


@router.get(
    "/{result_id}",
    response_model=schemas.ExaminationResultResponse
)
def get_examination_result(
    result_id: int,
    db: Session = Depends(get_db)
):

    result = examination_result_service.get_examination_result(db, result_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Examination result not found"
        )

    return result


@router.post(
    "/",
    response_model=schemas.ExaminationResultResponse,
    status_code=201
)
def create_examination_result(
    result: schemas.ExaminationResultCreate,
    db: Session = Depends(get_db)
):

    return examination_result_service.create_examination_result(db, result)


@router.put(
    "/{result_id}",
    response_model=schemas.ExaminationResultResponse
)
def update_examination_result(
    result_id: int,
    result: schemas.ExaminationResultCreate,
    db: Session = Depends(get_db)
):

    updated_result = examination_result_service.update_examination_result(
        db,
        result_id,
        result
    )

    if updated_result is None:
        raise HTTPException(
            status_code=404,
            detail="Examination result not found"
        )

    return updated_result


@router.delete("/{result_id}")
def delete_examination_result(
    result_id: int,
    db: Session = Depends(get_db)
):

    deleted_result = examination_result_service.delete_examination_result(db, result_id)

    if deleted_result is None:
        raise HTTPException(
            status_code=404,
            detail="Examination result not found"
        )

    return {
        "message": "Examination result deleted successfully"
    }