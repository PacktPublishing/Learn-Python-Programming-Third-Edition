# train-project/train_schedule/models/stations.py
from .event import Event


class StationsModel:
    """The StationsModel is in charge of keeping track of all the
    stations."""

    def __init__(self, datasource):
        self._datasource = datasource
        self._stations = {}
        self.updated = Event()

    def update(self):
        """Update the stations.

        Request updated station data from the data source and emit
        an `updated` event when the data is updated"""
        self._stations = {
            station.id: station
            for station in self._datasource.get_stations()
        }
        self.updated.emit(stations=self._stations.values())

    def get_station(self, station_id):
        """Retrieve a station by its `station_id`"""
        return self._stations.get(station_id)
