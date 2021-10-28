# train-project/train_schedule/views/about.py
import tkinter as tk
from tkinter import ttk

from .. import ABOUT_TEXT, APP_TITLE
from .dialog import Dialog


class AboutDialog(Dialog):
    """A dialog to show information about the app"""

    Title = f"About {APP_TITLE}"

    def __init__(self, parent, icon):
        self.icon = icon
        super().__init__(parent, self.Title, resizable=False)

    def create_widgets(self, body):
        """Create widgets to display the app icon and about
        text"""
        text_label = ttk.Label(
            body,
            image=self.icon,
            text=ABOUT_TEXT,
            compound=tk.LEFT,
        )
        text_label.grid(row=0, column=0, sticky=tk.NSEW)

        body.rowconfigure(0, weight=1)
        body.columnconfigure(0, weight=1)

    def create_buttons(self, buttonbox):
        """Create an OK button to close the dialog"""
        button = ttk.Button(
            buttonbox,
            text="OK",
            command=self.dismiss,
            default=tk.ACTIVE,
        )
        self.dialog.bind("<Return>", lambda e: button.invoke())

        button.grid(row=0, column=0, sticky=tk.NS)
        buttonbox.columnconfigure(0, weight=1)

        self.initial_focus = button
