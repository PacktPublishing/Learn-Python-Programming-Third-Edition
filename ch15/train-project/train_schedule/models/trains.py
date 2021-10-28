# train-project/train_schedule/models/trains.py
from .event import Event


class TrainsModelBase:
    """Base class for models that handle trains."""

    def __init__(self, datasource):
        self._datasource = datasource

        self._station = None
        self._trains = {}
        self.updated = Event()

    def set_station(self, station):
        """Set the station whose trains we are responsible for"""
        self._station = station
        self.update()

    def update(self):
        """Update the train data.

        If we have a station set, fetch trains for that station,
        otherwise clear the train data. Emit an `updated` event
        when the data is updated"""
        if self._station is not None:
            self._trains = {
                train.id: train for train in self._fetch_trains()
            }
        else:
            self._trains = {}

        self.updated.emit(trains=self._trains.values())

    def _fetch_trains(self):
        """Fetch trains from the datasource.

        This must be implemented by subclasses"""
        raise NotImplementedError

    def get_train(self, train_id):
        """Get a train by its `train_id`"""
        return self._trains[train_id]


class ArrivalsModel(TrainsModelBase):
    """The ArrivalsModel is in charge of keeping track of trains
    arriving at a station"""

    def _fetch_trains(self):
        """Fetch arrivals for our station from the datasource"""
        return self._datasource.get_arrivals(self._station.id)


class DeparturesModel(TrainsModelBase):
    """The DeparturesModel is in charge of keeping track of trains
    departing from a station"""

    def _fetch_trains(self):
        """Fetch departures for our station from the datasource"""
        return self._datasource.get_departures(self._station.id)
