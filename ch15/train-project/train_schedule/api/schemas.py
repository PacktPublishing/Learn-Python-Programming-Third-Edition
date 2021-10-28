# train-project/train_schedule/api/schemas.py
"""Pydantic schemas for objects received from the API"""
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ModelListMixin:
    """A mixin class to proxy container type dunder methods to the
    __root__ attribute of a pydantic model with a custom root
    type.

    See
    https://docs.python.org/3/reference/datamodel.html#emulating-container-types
    and
    https://pydantic-docs.helpmanual.io/usage/models/#custom-root-types
    """

    def __iter__(self):
        return iter(self.__root__)

    def __len__(self):
        return len(self.__root__)

    def __reversed__(self):
        return reversed(self.__root__)

    def __contains__(self, item):
        return item in self.__root__

    def __getitem__(self, item):
        return self.__root__[item]


class Station(BaseModel):
    """A class to represent a station.

    This should match the API response schema for a station"""

    id: int
    code: str
    country: str
    city: str


class StationList(ModelListMixin, BaseModel):
    """A list of stations."""

    __root__: List[Station]


class Train(BaseModel):
    """A class to represent trains

    This should match the API response schema for a train"""

    id: int
    id: int
    name: str
    station_from: Optional[Station] = None
    station_to: Optional[Station] = None
    departs_at: datetime
    arrives_at: datetime
    first_class: int
    second_class: int
    seats_per_car: int


class TrainList(ModelListMixin, BaseModel):
    """A list of trains"""

    __root__: List[Train]
