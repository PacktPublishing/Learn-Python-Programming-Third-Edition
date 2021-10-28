# train-project/train_schedule/metadata.py
"""Helper module to access package metadata"""
from importlib.metadata import PackageNotFoundError, metadata


def get_metadata():
    try:
        # Attempt to extract metadata from the installed package
        meta = metadata(__package__)
    except PackageNotFoundError:
        # If the package has not been installed, we get
        # a `PackageNotFoundError` exception. In this case,
        # we fall back to dummy values
        meta = {
            "Name": __package__.replace("_", "-"),
            "Summary": "description",
            "Author": "author",
            "Version": "version",
            "License": "license",
        }

    return meta
