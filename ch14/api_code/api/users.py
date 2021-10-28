# api_code/api/users.py
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
from .deps import Settings, get_db, get_settings
from .schemas import (
    Auth,
    AuthToken,
    Ticket,
    User,
    UserCreate,
    UserUpdate,
)
from .util import InvalidToken, create_token, extract_payload

router = APIRouter(prefix="/users")


@router.get("", response_model=list[User], tags=["Users"])
def get_users(
    db: Session = Depends(get_db), email: Optional[str] = None
):
    return crud.get_users(db=db, email=email)


@router.get("/{user_id}", response_model=User, tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} not found.",
        )
    return db_user


@router.get(
    "/{user_id}/tickets",
    response_model=list[Ticket],
    tags=["Users"],
)
def get_user_tickets(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} not found.",
        )
    return db_user.tickets


@router.post(
    "",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User {user.email} already exists.",
        )
    return crud.create_user(db=db, user=user)


@router.put("/{user_id}", response_model=User, tags=["Users"])
def update_user(
    user_id: int, user: UserUpdate, db: Session = Depends(get_db)
):
    db_user = crud.get_user(db=db, user_id=user_id)

    if db_user is None:
        db_user = crud.get_user_by_email(db, user.email)

        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User {user.email} already exists.",
            )

        else:
            crud.create_user(db=db, user=user, user_id=user_id)
            return Response(status_code=status.HTTP_201_CREATED)

    else:
        crud.update_user(db=db, user=user, user_id=user_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{user_id}", tags=["Users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    row_count = crud.delete_user(db=db, user_id=user_id)
    if row_count:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/authenticate", tags=["Auth"])
def authenticate(
    auth: Auth,
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
):
    db_user = crud.get_user_by_email(db=db, email=auth.email)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {auth.email} not found.",
        )

    if not db_user.is_valid_password(auth.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong username/password.",
        )

    payload = {
        "email": auth.email,
        "role": db_user.role.value,
    }
    return create_token(payload, settings.secret_key)


@router.post("/validate_token", tags=["Auth"])
def validate_token(
    auth: AuthToken,
    settings: Settings = Depends(get_settings),
):
    try:
        return extract_payload(auth.token, settings.secret_key)
    except InvalidToken as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid token: {err}",
        )
