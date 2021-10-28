# train-project/train_schedule/resources.py
"""Helper module to access package data resources"""
from importlib import resources


def load_binary_resource(name):
    """Load binary data from the named package data file

    This is analogous to doing

    with open(name, "rb") as stream:
        return stream.read()
    """
    return resources.read_binary(__package__, name)
