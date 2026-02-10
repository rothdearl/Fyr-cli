"""Regular expression source strings used throughout the command-line interface package."""

from typing import Final, final


@final
class Patterns:
    """
    Namespace for regular expression source strings.

    :cvar DIGITS: Matches one or more ASCII digits.
    :cvar NON_ALPHANUMERIC: Matches sequences of non-alphanumeric characters.
    :cvar NON_SPACE_WHITESPACE: Matches non-space whitespace characters.
    :cvar NO_MATCH: Matches nothing.
    :cvar WORD: Matches a whole word token.
    :cvar WORD_SEPARATOR: Matches one or more non-word characters.
    """
    DIGITS: Final[str] = r"[0-9]+"
    NON_ALPHANUMERIC: Final[str] = r"[^a-zA-Z0-9]+"
    NON_SPACE_WHITESPACE: Final[str] = r"[\f\r\n\t\v]+"
    NO_MATCH: Final[str] = r"(?!.)"
    WORD: Final[str] = r"\b\w+\b"
    WORD_SEPARATOR: Final[str] = r"\W+"


__all__ = [
    "Patterns",
]
