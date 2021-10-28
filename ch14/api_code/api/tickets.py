# api_code/api/tickets.py
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
from .schemas import Ticket, TicketCreate

router = APIRouter(prefix="/tickets")


@router.get("", response_model=list[Ticket], tags=["Tickets"])
def get_tickets(db: Session = Depends(get_db)):
    return crud.get_tickets(db=db)


@router.get(
    "/{ticket_id}", response_model=Ticket, tags=["Tickets"]
)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = crud.get_ticket(db=db, ticket_id=ticket_id)
    if db_ticket is None:
        raise HTTPException(
            status_code=404,
            detail=f"Ticket {ticket_id} not found.",
        )
    return db_ticket


@router.post(
    "",
    response_model=Ticket,
    status_code=status.HTTP_201_CREATED,
    tags=["Tickets"],
)
def create_ticket(
    ticket: TicketCreate, db: Session = Depends(get_db)
):
    return crud.create_ticket(db=db, ticket=ticket)


@router.delete("/{ticket_id}", tags=["Tickets"])
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    row_count = crud.delete_ticket(db=db, ticket_id=ticket_id)
    if row_count:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_404_NOT_FOUND)
