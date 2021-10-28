# train-project/train_schedule/views/main.py
import tkinter as tk
from contextlib import contextmanager
from tkinter import messagebox, ttk

from .. import APP_TITLE
from ..resources import load_binary_resource
from .stations import StationChooser
from .trains import TrainsView

ICON_FILENAME = "icon.png"


@contextmanager
def show_error():
    """A simple context manager to catch any exceptions and
    display them as error messages in an error dialog"""
    try:
        yield
    except Exception as error:
        messagebox.showerror(title="Error", message=error)


class MainWindow:
    """The main window for our app"""

    def __init__(self):
        self.root = tk.Tk()

        self._set_title()
        self._set_icon()

        self._make_menus()
        content_frame = self._make_content()

        self._layout_widgets(content_frame)

    def _set_title(self):
        """Set the window title"""
        self.title = APP_TITLE
        self.root.title(self.title)
        self.root.iconname(self.title)

    def _set_icon(self):
        """Set the window icon"""
        self.icon = tk.PhotoImage(
            data=load_binary_resource(ICON_FILENAME)
        )
        self.root.iconphoto(True, self.icon)

    def _make_menus(self):
        """Create the menubar"""
        self.root.option_add("*tearOff", False)
        self.menubar = tk.Menu(self.root)

        self._make_app_menu()
        self._make_edit_menu()
        self._make_help_menu()

        self.root["menu"] = self.menubar

    def _make_app_menu(self):
        """Create the main application menu"""
        app_menu = tk.Menu(self.menubar)
        app_menu.add_command(
            label="Refresh",
            command=lambda: self.root.event_generate(
                "<<RefreshData>>"
            ),
            underline=0,
        )
        app_menu.add_command(
            label="Quit",
            command=self.quit,
            underline=0,
        )
        self.menubar.add_cascade(
            menu=app_menu, label=self.title, underline=0
        )

    def _make_edit_menu(self):
        """Create the 'Edit' menu"""
        edit_menu = tk.Menu(self.menubar)
        edit_menu.add_command(
            label="Preferences...",
            command=lambda: self.root.event_generate(
                "<<OpenPreferencesDialog>>"
            ),
            underline=0,
        )
        self.menubar.add_cascade(
            menu=edit_menu, label="Edit", underline=0
        )

    def _make_help_menu(self):
        """Create the 'Help' menu"""
        help_menu = tk.Menu(self.menubar)
        help_menu.add_command(
            label="About...",
            command=lambda: self.root.event_generate(
                "<<OpenAboutDialog>>"
            ),
            underline=0,
        )
        self.menubar.add_cascade(
            menu=help_menu, label="Help", underline=0
        )

    def _make_content(self):
        """Create the widgets to populate the body of the
        window"""
        content_frame = ttk.Frame(self.root, padding=(5, 5, 5, 5))
        station_frame = self._make_station_chooser(content_frame)
        station_frame.grid(row=0, column=0, sticky=tk.NSEW)

        notebook = ttk.Notebook(
            content_frame, padding=(0, 5, 0, 0)
        )
        self.arrivals_view = self._make_train_tab(
            notebook, "Arrivals", show_from=True, show_to=False
        )

        self.departures_view = self._make_train_tab(
            notebook, "Departures", show_from=False, show_to=True
        )
        notebook.grid(row=1, column=0, sticky=tk.NSEW)

        content_frame.rowconfigure(1, weight=1)
        content_frame.columnconfigure(0, weight=1)

        return content_frame

    def _make_station_chooser(self, content_frame):
        """Create the station chooser dropdown"""
        station_frame = ttk.LabelFrame(
            content_frame, text="Station", padding=(5, 5, 5, 5)
        )
        self.station_chooser = StationChooser(station_frame)
        self.station_chooser.combobox.grid(
            row=0, column=0, sticky=tk.NSEW
        )
        station_frame.columnconfigure(0, weight=1)

        return station_frame

    def _make_train_tab(self, notebook, name, show_from, show_to):
        """Create the widgets to display either arrivals or
        departures"""
        frame = ttk.Frame(notebook, padding=(5, 5, 5, 5))
        notebook.add(frame, text=name)

        train_view = TrainsView(
            frame, show_from=show_from, show_to=show_to
        )
        scrollbar = ttk.Scrollbar(
            frame,
            orient=tk.VERTICAL,
            command=train_view.treeview.yview,
        )
        train_view.treeview.configure(
            yscrollcommand=scrollbar.set
        )

        train_view.treeview.grid(row=0, column=0, sticky=tk.NSEW)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        return train_view

    def _layout_widgets(self, content_frame):
        """Lay out the main frame of the window"""
        content_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

    def bind(self, *args, **kwargs):
        """Proxy for the underlying window's bind method"""
        self.root.bind(*args, *kwargs)

    def unbind(self, *args, **kwargs):
        """Proxy for the underlying window's unbind method"""
        self.root.unbind(*args, *kwargs)

    def run(self):
        """Run the main loop"""
        self.root.mainloop()

    def quit(self, event=None):
        """Destroy the window and quit the app"""
        self.root.destroy()
