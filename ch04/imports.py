# imports.py
from datetime import datetime, timezone  # two imports on the same line
from unittest.mock import patch  # single import

import pytest  # third party library

from core.models import (  # multiline import
    Exam,
    Exercise,
    Solution,
)

print(datetime.date)
print(timezone.tzname)
