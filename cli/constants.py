"""
Module for defining constants used throughout the command-line interface package.
"""

import os
from typing import Final

OS_IS_WINDOWS: Final[bool] = os.name == "nt"
