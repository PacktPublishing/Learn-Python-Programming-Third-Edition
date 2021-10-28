# train-project/train_schedule/views/dialog.py
import tkinter as tk
from tkinter import ttk


class Dialog:
    """Base class for dialogs.

    Subclasses should override the `create_widgets` method to
    populate the body of the dialog and the `create_buttons` to
    populate the button area at the bottom of the dialog.

    The `initial_focus` attribute can be set to the widget that
    should get focus when the dialog is displayed.

    To display the dialog, call the `run` method.

    To close and destroy the dialog, call `dismiss`.
    """

    def __init__(self, parent, title, resizable=False):
        self.dialog = tk.Toplevel(
            parent, class_=self.__class__.__name__
        )

        self._title = title
        self._resizable = resizable

        self.dialog.withdraw()
        self.dialog.transient(parent)

        self._set_title()

        body = ttk.Frame(self.dialog, padding=(5, 5, 5, 5))
        buttonbox = ttk.Frame(self.dialog, padding=(5, 5, 5, 5))
        self._layout_widgets(body, buttonbox)

        self.initial_focus = body
        self.create_widgets(body)
        self.create_buttons(buttonbox)

        self.dialog.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.dialog.bind("<Escape>", self.dismiss)

    def _set_title(self):
        """Set the dialog title.

        This is called automatically when the dialog is created"""
        self.dialog.title(self._title)
        self.dialog.iconname(self._title)

    def _layout_widgets(self, body, buttonbox):
        """Lay out the frames containing the dialog body and
        buttons"""
        body.grid(row=0, column=0, sticky=tk.NSEW)
        buttonbox.grid(row=1, column=0, sticky=tk.NSEW)

        self.dialog.rowconfigure(0, weight=1)
        self.dialog.rowconfigure(1, weight=0)
        self.dialog.columnconfigure(0, weight=1)

    def create_widgets(self, body):
        """Create the widgets for the dialog body

        Subclasses should override this method."""
        pass

    def create_buttons(self, buttonbox):
        """Create the buttons to show at the bottom of the dialog

        Subclasses should override this method."""
        pass

    def dismiss(self, event=None):
        """Close and destroy the dialog"""
        self.dialog.grab_release()
        self.dialog.destroy()

    def run(self):
        """Run the dialog"""
        self.dialog.deiconify()
        self.initial_focus.focus_set()
        self.dialog.wait_visibility()
        self.dialog.resizable(
            width=self._resizable, height=self._resizable
        )
        self.dialog.grab_set()
        self.dialog.wait_window()

    def bind(self, *args, **kwargs):
        """Proxy for the underlying window's bind method"""
        self.dialog.bind(*args, **kwargs)

    def unbind(self, *args, **kwargs):
        """Proxy for the underlying window's unbind method"""
        self.dialog.unbind(*args, **kwargs)
