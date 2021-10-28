# train-project/train_schedule/gui.py
from .api import TrainAPIClient
from .config import load_config, save_config
from .models.stations import StationsModel
from .models.trains import ArrivalsModel, DeparturesModel
from .views.about import AboutDialog
from .views.config import ConfigDialog
from .views.main import MainWindow, show_error


def main():
    """Launch the GUI"""
    train_app = TrainApp()
    train_app.run()


class TrainApp:
    """This class is the main controller of the train schedule
    application.

    It is responsible for creating the models and the views and
    handling/coordinating interaction between them.
    """

    def __init__(self):
        self.config = load_config()

        self.api_client = TrainAPIClient(self.config)

        # Create models
        self.stations_model = StationsModel(
            datasource=self.api_client
        )
        self.arrivals_model = ArrivalsModel(
            datasource=self.api_client,
        )
        self.departures_model = DeparturesModel(
            datasource=self.api_client,
        )

        # Bind callbacks to handle model events
        self.stations_model.updated.bind(self.stations_updated)
        self.arrivals_model.updated.bind(self.arrivals_updated)
        self.departures_model.updated.bind(
            self.departures_updated
        )

        # Create the main window
        self.mainwindow = MainWindow()

        # Handy aliases to refer to some main window attributes
        self.root = self.mainwindow.root
        self.icon = self.mainwindow.icon
        self.station_chooser = self.mainwindow.station_chooser
        self.arrivals_view = self.mainwindow.arrivals_view
        self.departures_view = self.mainwindow.departures_view

        # Register callbacks to handle UI events
        self.mainwindow.bind("<Visibility>", self.main_visible)
        self.mainwindow.bind("<<OpenAboutDialog>>", self.about)
        self.mainwindow.bind(
            "<<OpenPreferencesDialog>>", self.configure
        )
        self.mainwindow.bind("<<RefreshData>>", self.refresh)
        self.station_chooser.bind(
            "<<ComboboxSelected>>", self.station_selected
        )

    def run(self):
        self.mainwindow.run()

    def main_visible(self, event=None):
        """Event handler to perform actions that should take
        place when the main window is first displayed. We will
        immediately unbind the window "<Visibility>" event, so
        that this handler does not get called again after the
        window is hidden (e.g. minimised) and displayed again.
        """
        self.mainwindow.unbind("<Visibility>")

        # If we have an API url configured, call `refresh` to
        # fetch data from the API. Otherwise, show the `configure`
        # dialog to prompt the user to enter an API URL.
        if self.config.api_url:
            self.refresh()
        else:
            self.configure()

    def station_selected(self, event=None):
        """Event handler to invoke when a station is selected."""
        self.update_trains()

    def refresh(self, event=None):
        """Handler to refresh our data"""
        # We only need to update the stations here. We'll update
        # the trains after stations are updated (when we get
        # a `updated` event from the stations model).
        self.update_stations()

    def about(self, event=None):
        """Show the about dialog"""
        about_dialog = AboutDialog(self.root, self.icon)
        about_dialog.run()

    def configure(self, event=None):
        """Show the configuration dialog"""
        config_dialog = ConfigDialog(self.root, self.config)
        config_dialog.bind(
            "<<ConfigUpdated>>", self.config_updated
        )
        config_dialog.run()

    def config_updated(self, event=None):
        """Handler for when the configuration is updated.

        Whenever the config is updated, we need to save the config
        and refresh our data"""
        with show_error():
            save_config(self.config)
        self.refresh()

    def stations_updated(self, stations):
        """Handler for when the stations model is updated.

        We need to update the station chooser with the new
        station list and then update the trains"""
        self.station_chooser.set_stations(stations)
        self.update_trains()

    def arrivals_updated(self, trains):
        """Handler for when the arrivals model is updated.

        We need to update the arrivals view with the new trains
        list"""
        self.arrivals_view.set_trains(trains)

    def departures_updated(self, trains):
        """Handler for when the departures model is updated.

        We need to update the departures view with the new trains
        list"""
        self.departures_view.set_trains(trains)

    def update_stations(self):
        """Tell the stations model to update itself"""
        with show_error():
            self.stations_model.update()

    def update_trains(self):
        """Update the arrivals and departures models.

        Get the currently selected station and update the arrivals
        and departures models with that station"""
        station_id = self.station_chooser.get_selected()
        with show_error():
            station = self.stations_model.get_station(station_id)
            self.arrivals_model.set_station(station)
            self.departures_model.set_station(station)
