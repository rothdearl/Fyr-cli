"""
Type aliases used throughout the command-line interface package.
"""

import re
from collections.abc import Callable
from typing import Any

type ErrorReporter = Callable[[str], None]
"""Callback for reporting error messages."""

type JsonObject = dict[str, Any]
"""A decoded JSON object represented as a dictionary."""

type Patterns = list[re.Pattern[str]]
"""List of compiled regular expression patterns."""

__all__ = [
    "ErrorReporter",
    "JsonObject",
    "Patterns",
]
