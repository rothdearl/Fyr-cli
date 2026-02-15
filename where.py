#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A program that displays current IP-based location information."""

import argparse
import sys
from typing import Final

import requests

from cli import JsonObject


def build_arguments() -> argparse.ArgumentParser:
    """Build and return an argument parser."""
    parser = argparse.ArgumentParser(allow_abbrev=False, description="display current ip-based location information",
                                     prog=Where.NAME)

    parser.add_argument("-c", "--coordinates", action="store_true",
                        help="display geographic coordinates")
    parser.add_argument("--ip", action="store_true", help="display public ip address")
    parser.add_argument("--version", action="version", version=f"%(prog)s {Where.VERSION}")

    return parser


def get_json_value(*, data: JsonObject, key: str) -> str:
    """Return the string value for a key in the JSON data, or ``"n/a"`` if the key is missing."""
    return data.get(key, "n/a")


class Where:
    """
    A program that displays current IP-based location information.

    :cvar IPINFO_URL: Endpoint returning public IP geolocation data in JSON.
    :cvar NAME: Program name.
    :cvar VERSION: Program version.
    :ivar args: Parsed command-line arguments.
    """

    IPINFO_URL: Final[str] = "https://ipinfo.io/json"
    NAME: Final[str] = "where"
    VERSION: Final[str] = "1.0.0"

    def __init__(self) -> None:
        """Initialize a new ``Where`` instance."""
        self.args: argparse.Namespace = build_arguments().parse_args()

    def main(self) -> None:
        """Run the program."""
        try:
            response = requests.get(Where.IPINFO_URL, timeout=5)

            # Ensure a successful response.
            response.raise_for_status()

            # Get JSON data.
            data = response.json()

            # Print geolocation information.
            for key in ("city", "region", "postal", "country", "timezone"):
                print(f"{key}: {get_json_value(data=data, key=key)}")

            # Optionally print geographic location and public IP address.
            if self.args.coordinates:  # --coordinates
                print(f"coordinates: {get_json_value(data=data, key='loc')}")

            if self.args.ip:  # --ip
                print(f"ip: {get_json_value(data=data, key='ip')}")
        except requests.RequestException:
            print(f"{Where.NAME}: error: unable to retrieve location", file=sys.stderr)
            raise SystemExit(1)


if __name__ == "__main__":
    Where().main()
