# api_code/api/trains.py
from typing import Optional

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,
    status,
)
from sqlalchemy.orm import Session

from . import crud
from .deps import get_db
from .schemas import Ticket, Train, TrainCreate

router = APIRouter(prefix="/trains")


@router.get("", response_model=list[Train], tags=["Trains"])
def get_trains(
    db: Session = Depends(get_db),
    station_from_code: str = None,
    station_to_code: str = None,
    include_all: Optional[bool] = False,
):
    return crud.get_trains(
        db=db,
        station_from_code=station_from_code,
        station_to_code=station_to_code,
        include_all=include_all,
    )


@router.get("/{train_id}", response_model=Train, tags=["Trains"])
def get_train(train_id: int, db: Session = Depends(get_db)):
    db_train = crud.get_train(db=db, train_id=train_id)
    if db_train is None:
        raise HTTPException(
            status_code=404, detail=f"Train {train_id} not found."
        )
    return db_train


@router.get(
    "/{train_id}/tickets",
    response_model=list[Ticket],
    tags=["Tickets"],
)
def get_train_tickets(
    train_id: int, db: Session = Depends(get_db)
):
    db_train = crud.get_train(db=db, train_id=train_id)
    if db_train is None:
        raise HTTPException(
            status_code=404, detail=f"Train {train_id} not found."
        )
    return db_train.tickets


@router.post(
    "",
    response_model=Train,
    status_code=status.HTTP_201_CREATED,
    tags=["Trains"],
)
def create_train(
    train: TrainCreate, db: Session = Depends(get_db)
):
    db_train = crud.get_train_by_name(db=db, name=train.name)
    if db_train:
        raise HTTPException(
            status_code=400,
            detail=f"Train {train.name} already exists.",
        )
    return crud.create_train(db=db, train=train)


@router.delete("/{train_id}", tags=["Trains"])
def delete_user(train_id: int, db: Session = Depends(get_db)):
    row_count = crud.delete_train(db=db, train_id=train_id)
    if row_count:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_404_NOT_FOUND)
