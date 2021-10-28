# train-project/train_schedule/__main__.py
"""Enable using `python -m train_schedule` to launch the app.

If any command-line arguments are provided, we launch the command
line interface. If no command-line arguments are present, launch
the GUI instead.
"""
import sys

from .cli import main as cli_main
from .gui import main as gui_main

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cli_main()
    else:
        gui_main()


"""
$ python -m train_schedule stations
0: Rome, Italy (ROM)
1: Paris, France (PAR)
2: London, UK (LDN)
3: Kyiv, Ukraine (KYV)
4: Stockholm, Sweden (STK)
5: Warsaw, Poland (WSW)
6: Moskow, Russia (MSK)
7: Amsterdam, Netherlands (AMD)
8: Edinburgh, Scotland (EDB)
9: Budapest, Hungary (BDP)
10: Bucharest, Romania (BCR)
11: Sofia, Bulgaria (SFA)
"""
