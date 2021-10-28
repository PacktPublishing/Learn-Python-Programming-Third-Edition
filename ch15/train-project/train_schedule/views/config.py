# train-project/train_schedule/views/config.py
import tkinter as tk
from tkinter import ttk

from .. import APP_TITLE
from .dialog import Dialog


class ConfigDialog(Dialog):
    """A configuration dialog"""

    Title = f"{APP_TITLE} Configuration"

    def __init__(self, parent, config):
        self.config = config

        super().__init__(parent, title=self.Title, resizable=True)

    def create_widgets(self, body):
        """Create widgets to allow the user to set configuration
        values"""
        self._make_config_vars()

        url_frame = ttk.LabelFrame(
            body,
            text="Train API URL",
            padding=(5, 5, 5, 5),
        )

        url_entry = ttk.Entry(
            url_frame,
            width=40,
            textvariable=self._config_vars["api_url"],
        )
        url_entry.grid(row=0, column=0, sticky=tk.NSEW)
        url_frame.columnconfigure(0, weight=1)

        url_frame.grid(row=0, column=0, sticky=tk.NSEW)
        body.columnconfigure(0, weight=1)

        self.initial_focus = url_entry

    def create_buttons(self, buttonbox):
        """Create OK and cancel buttons"""
        ok_button = ttk.Button(
            buttonbox,
            text="OK",
            command=self.ok,
            default=tk.ACTIVE,
        )
        self.dialog.bind("<Return>", lambda e: ok_button.invoke())

        cancel_button = ttk.Button(
            buttonbox, text="Cancel", command=self.dismiss
        )

        cancel_button.grid(
            row=0, column=0, sticky=(tk.N, tk.S, tk.E)
        )
        ok_button.grid(row=0, column=1, sticky=tk.NSEW)
        buttonbox.columnconfigure(0, weight=1)

    def _make_config_vars(self):
        """Create Tk variables for all the configuration values"""
        self._config_vars = {
            "api_url": tk.StringVar(
                self.dialog, self.config.api_url, "api_url"
            ),
        }

    def _update_config(self):
        """Update the configuration from the Tk variables and emit
        a `<<ConfigUpdated>>` event if the config has changed"""
        changed = False
        for key, var in self._config_vars.items():
            orig = getattr(self.config, key)
            setattr(self.config, key, var.get())
            changed |= orig != getattr(self.config, key)

        if changed:
            self.dialog.event_generate("<<ConfigUpdated>>")

    def ok(self):
        """Handler for when the OK button is clicked"""
        self._update_config()
        self.dismiss()
