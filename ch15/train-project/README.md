# Train Schedule

A train schedule application to demonstrate packaging and distribution of a Python project for
Chapter 15 of "Learn Python Programming, 3d Edition", by Fabrizio Romano and Heinrich Kruger. At the
same time, it acts as an example of an application built around the trains API project from Chapter
14 of the same book.

## Usage

The application provides both command-line and graphical interfaces.

### Graphical interface

To launch the train schedule GUI, run:

    $ train-schedule

This will allow you to select a station from a drop-down list and show you listings of trains
arriving at and departing from the selected station.

The Train API URL can be configured via the `Edit > Preferences` menu option.

### Command-line interface

The command-line interface can be invoked via:

    $ train-schedule-cli

If no command-line arguments are provided, a brief usage message will be printed. More detailed help
can be obtained by passing `-h` or `--help` as a command-line argument.

#### Configuration

The command-line and graphical interfaces share the same configuration file. To view the current
configuration, you can run:

    $ train-schedule-cli config

To update the Train API URL, use:

    $ train-schedule-cli config --api-url URL

Where `URL` is the new URL to use.

#### Listing stations

To get a list of available stations, run

    $ train-schedule-cli stations

#### Listing arrivals

To see a list of trains arriving at a station, run:

    $ train-schedule-cli --arrivals station-id

Where `station-id` is the numeric ID of the station.

#### Listing departures

To see departures from a station you can use:

    $ train-schedule-cli --departures station-id
