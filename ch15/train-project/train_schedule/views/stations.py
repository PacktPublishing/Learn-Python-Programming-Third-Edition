# train-project/train_schedule/views/stations.py
import tkinter as tk
from tkinter import ttk

from . import formatters


class StationChooser:
    """Display stations in a dropdown selector"""

    def __init__(self, parent):
        self._station_var = tk.StringVar(value="", name="station")
        self.combobox = ttk.Combobox(
            parent,
            textvariable=self._station_var,
            state=["readonly"],
        )

        # We keep a list of the station_ids in the same order as
        # the stations in our combobox. This will allow us to look
        # up the ID of the currently selected station.
        self._station_ids = []

    def set_stations(self, stations):
        """Set the stations that can be chosen"""

        # We need to keep our list of station_ids in sync with the
        # combobox. To do this, we clear the _station_ids list and
        # repopulate the list with the new station IDs.
        self._station_ids.clear()
        values = []

        for station in stations:
            values.append(formatters.format_station(station))
            self._station_ids.append(station.id)

        self.combobox["values"] = values

    def get_selected(self):
        """Get the ID of the selected station"""
        # Get the position of the currently selected item
        selection_idx = self.combobox.current()

        if selection_idx == -1:
            # Nothing is selected
            selected_id = None
        else:
            # Look up the ID of the selected item in our
            # _station_ids list.
            selected_id = self._station_ids[selection_idx]

        return selected_id

    def bind(self, *args, **kwargs):
        """Proxy for the underlying combobox's bind method"""
        self.combobox.bind(*args, **kwargs)

    def unbind(self, *args, **kwargs):
        """Proxy for the underlying combobox's unbind method"""
        self.combobox.unbind(*args, **kwargs)
