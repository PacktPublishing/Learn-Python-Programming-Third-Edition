# api_code/api/schemas.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from . import models

# USERS


class Auth(BaseModel):
    email: str
    password: str


class AuthToken(BaseModel):
    token: str


class UserBase(BaseModel):
    full_name: str
    email: str
    role: models.Roles


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
        use_enum_values = True


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    full_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[models.Roles] = None


# STATIONS


class StationBase(BaseModel):
    code: str
    country: str
    city: str


class Station(StationBase):
    id: int

    class Config:
        orm_mode = True


class StationCreate(StationBase):
    pass


class StationUpdate(StationBase):
    code: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None


# TRAINS


class TrainBase(BaseModel):
    name: str
    station_from: Optional[Station] = None
    station_to: Optional[Station] = None
    departs_at: datetime
    arrives_at: datetime
    first_class: int
    second_class: int
    seats_per_car: int


class Train(TrainBase):
    id: int

    class Config:
        orm_mode = True


class TrainCreate(TrainBase):
    station_from_id: int
    station_to_id: int


# TICKETS


class TicketBase(BaseModel):
    user_id: int
    train_id: int
    price: float
    car_class: models.Classes


class Ticket(TicketBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
        use_enum_values = True


class TicketCreate(TicketBase):
    pass
