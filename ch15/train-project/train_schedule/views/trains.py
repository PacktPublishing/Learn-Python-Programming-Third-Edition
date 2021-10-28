# train-project/train_schedule/views/trains.py
import tkinter as tk
from tkinter import ttk

from . import formatters


class TrainsView:
    """Display information about trains in a table"""

    def __init__(self, parent, show_from=True, show_to=True):
        self._columns = formatters.TrainAttributeNames.copy()

        if not show_from:
            del self._columns["station_from"]

        if not show_to:
            del self._columns["station_to"]

        self.treeview = ttk.Treeview(
            parent,
            columns=list(self._columns.keys()),
            show="headings",
            selectmode=tk.BROWSE,
        )

        for column_id, heading in self._columns.items():
            self.treeview.heading(column_id, text=heading)

    def set_trains(self, trains):
        """Set the trains to be displayed"""
        self.clear()
        for train in trains:
            self.add_train(train)

    def clear(self):
        """Remove all trains from the view"""
        children = self.treeview.get_children("")
        self.treeview.delete(*children)

    def add_train(self, train):
        """Add a train to the view"""
        self.treeview.insert(
            "",
            tk.END,
            str(train.id),
            values=tuple(self._format_columns(train)),
        )

    def _format_columns(self, train):
        """Format the data to be displayed in the table columns"""
        for col_name in self._columns:
            yield formatters.format_train_attr(train, col_name)
