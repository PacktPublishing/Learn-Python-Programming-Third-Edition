# train-project/train_schedule/__init__.py
from .metadata import get_metadata

_metadata = get_metadata()

# Extract some useful attributes from the package metadata
APP_NAME = _metadata["Name"]
APP_TITLE = APP_NAME.title()
VERSION = _metadata["Version"]
AUTHOR = _metadata["Author"]
DESCRIPTION = _metadata["Summary"]
LICENSE = _metadata["License"]

# Define text to be displayed in the GUI about dialog or via the
# CLI --about option
ABOUT_TEXT = f"""{APP_TITLE}

{DESCRIPTION}

Version: {VERSION}
Authors: {AUTHOR}
License: {LICENSE}
Copyright: © 2021 {AUTHOR}"""
