# train-project/train_schedule/api/__init__.py
from urllib.parse import urljoin

import requests

from .schemas import StationList, TrainList


class APIError(Exception):
    """An exception for errors coming from the API"""

    pass


class TrainAPIClient:
    """This is our interface to the trains API.

    The API client is in charge of our communication with the
    trains API. It knows which HTTP calls to make, to which API
    endpoints to get the data we need for our application."""

    STATIONS_PATH = "/stations"
    STATION_ARRIVALS_PATH = "/stations/{station_id}/arrivals"
    STATION_DEPARTURES_PATH = "/stations/{station_id}/departures"

    def __init__(self, config):
        self.config = config
        self._session = requests.Session()

    def get_stations(self):
        """Get a list of stations from the API"""
        url = self._make_url(self.STATIONS_PATH)
        return StationList.parse_obj(self._get(url))

    def get_arrivals(self, station_id):
        """Get a list of trains arriving at a particular
        station"""
        url = self._make_url(self.STATIONS_PATH)

        url = self._make_url(
            self.STATION_ARRIVALS_PATH, station_id=station_id
        )
        return TrainList.parse_obj(self._get(url))

    def get_departures(self, station_id):
        """Get a list of trains departing from a particular
        station"""
        url = self._make_url(
            self.STATION_DEPARTURES_PATH, station_id=station_id
        )
        return TrainList.parse_obj(self._get(url))

    def _make_url(self, path, **kwargs):
        """Construct a URL for an API request.

        Join the configured API url with the endpoint path,
        formatted with any arguments that may need to be
        substituted in."""
        if not self.config.api_url:
            raise APIError("No API URL configured")
        return urljoin(self.config.api_url, path.format(**kwargs))

    def _get(self, url):
        """Make an HTTP GET request.

        This method takes care of all the details of making a GET
        request to the api. It will handle any request errors (and
        raise an API error instead). If we get a successful
        response it will decode the JSON response.
        """

        try:
            response = self._session.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            try:
                msg = err.response.json()["detail"]
            except requests.exceptions.InvalidJSONError:
                msg = err.response.text()
            raise APIError(msg) from err
        except requests.exceptions.RequestException as err:
            raise APIError(f"Error connecting to {url}") from err
        else:
            return response.json()
