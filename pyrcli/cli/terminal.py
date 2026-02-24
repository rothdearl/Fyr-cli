"""Predicates describing whether the standard streams are attached to a terminal."""

import sys
from typing import Final


def stderr_is_redirected() -> bool:
    """Return whether standard error is redirected."""
    return not stderr_is_terminal()


def stderr_is_terminal() -> bool:
    """Return whether standard error is attached to a terminal."""
    return sys.stderr.isatty()


def stdin_is_redirected() -> bool:
    """Return whether standard input is redirected."""
    return not stdin_is_terminal()


def stdin_is_terminal() -> bool:
    """Return whether standard input is attached to a terminal."""
    return sys.stdin.isatty()


def stdout_is_redirected() -> bool:
    """Return whether standard output is redirected."""
    return not stdout_is_terminal()


def stdout_is_terminal() -> bool:
    """Return whether standard output is attached to a terminal."""
    return sys.stdout.isatty()


__all__: Final[tuple[str, ...]] = (
    "stderr_is_redirected",
    "stderr_is_terminal",
    "stdin_is_redirected",
    "stdin_is_terminal",
    "stdout_is_redirected",
    "stdout_is_terminal",
)
