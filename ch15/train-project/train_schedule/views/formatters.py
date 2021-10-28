# train-project/train_schedule/views/formatters.py
"""Helper functions to format data for display."""


def format_station(station, show_id=False):
    """Format station data for display"""
    if station is None:
        return "Unknown"
    else:
        fmt_str = "{city}, {country} ({code})"
        if show_id:
            fmt_str = "{id}: " + fmt_str

        return fmt_str.format(**station.dict())


def format_datetime(time_value):
    """Format a datetime according to the current locale"""
    return time_value.strftime("%c")


TrainFormatters = {
    "station_from": format_station,
    "station_to": format_station,
    "departs_at": format_datetime,
    "arrives_at": format_datetime,
}
"""Lookup table for functions to format various attributes of
a train"""


TrainAttributeNames = {
    "station_from": "From",
    "station_to": "To",
    "departs_at": "Departs",
    "arrives_at": "Arrives",
    "first_class": "1st class cars",
    "second_class": "2nd class cars",
    "seats_per_car": "Seats/car",
}
"""Lookup table for display names of train attributes"""


def format_train_attr(train, attr):
    """Format a train attribute"""
    value = getattr(train, attr)
    formatter = TrainFormatters.get(attr)

    if formatter:
        value = formatter(value)

    return value


def format_train(train, show_from=True, show_to=True):
    """Format train data for display"""
    columns = TrainAttributeNames.copy()
    if not show_from:
        del columns["station_from"]
    if not show_to:
        del columns["station_to"]

    return "\t".join(
        f"{heading}: {format_train_attr(train, attr)}"
        for attr, heading in columns.items()
    )
