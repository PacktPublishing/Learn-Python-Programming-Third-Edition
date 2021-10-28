# train-project/train_schedule/cli.py
"""This module defines the command line interface"""
import argparse

from . import (
    ABOUT_TEXT,
    APP_NAME,
    APP_TITLE,
    DESCRIPTION,
    VERSION,
)
from .api import TrainAPIClient
from .config import load_config, save_config
from .views import formatters


def main():
    """Launch the CLI"""
    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()

    if args.version:
        print_version()
    elif args.about:
        print_about()
    elif args.command == "config":
        configuration(api_url=args.api_url)
    elif args.command == "stations":
        list_stations()
    elif args.command == "arrivals":
        list_arrivals(station_id=args.station_id)
    elif args.command == "departures":
        list_departures(station_id=args.station_id)
    else:
        arg_parser.print_usage()


def get_arg_parser():
    """Configure command-line arguments"""
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        "-v",
        "--version",
        help="Print version information and exit",
        action="store_true",
    )

    parser.add_argument(
        "-a",
        "--about",
        help=f"Print information about {APP_NAME} and exit",
        action="store_true",
    )

    subcommands = parser.add_subparsers(
        title="Commands",
        dest="command",
        description=(
            "Use '%(prog)s COMMAND -h' to get help on a command"
        ),
    )

    config_parser = subcommands.add_parser(
        "config",
        description="View or update configuration",
        help="View or update configuration",
    )
    config_parser.add_argument(
        "-u",
        "--api-url",
        help="Update the Train API URL",
    )

    subcommands.add_parser(
        "stations",
        description="List available stations",
        help="List available stations",
    )

    station_id_args = argparse.ArgumentParser(add_help=False)
    station_id_args.add_argument(
        "station_id",
        help="The station ID",
        type=int,
    )

    subcommands.add_parser(
        "arrivals",
        description="List arrivals for a station",
        help="List arrivals for a station",
        parents=[station_id_args],
    )

    subcommands.add_parser(
        "departures",
        description="List departures for a station",
        help="List departures for a station",
        parents=[station_id_args],
    )

    return parser


def print_version():
    """Print the app version"""
    print(f"{APP_TITLE} {VERSION}")


def print_about():
    """Print about message"""
    print(ABOUT_TEXT)


def configuration(api_url):
    """Show or update the configuration"""
    config = load_config()

    if api_url is not None:
        config.api_url = api_url
        save_config(config)
    else:
        print(config)


def list_stations():
    """Print a list of stations"""
    api_client = TrainAPIClient(load_config())

    stations = api_client.get_stations()
    for station in stations:
        print(formatters.format_station(station, show_id=True))


def list_arrivals(station_id):
    """Print a listing of trains arriving at a station"""
    api_client = TrainAPIClient(load_config())

    arrivals = api_client.get_arrivals(station_id)
    for train in arrivals:
        print(formatters.format_train(train, show_to=False))


def list_departures(station_id):
    """Print a listing of trains departing from a station"""
    api_client = TrainAPIClient(load_config())

    departures = api_client.get_departures(station_id)
    for train in departures:
        print(formatters.format_train(train, show_from=False))
