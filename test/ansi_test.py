#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from typing import final

from cli import ansi


@final
class ANSITest(unittest.TestCase):
    """
    Tests the ansi module.
    """

    def test_256_color_palette(self) -> None:
        self.assertEqual(len(ansi.TEXT_ATTRIBUTES), 9)
        self.assertEqual(len(ansi.BG_COLORS_16), 16)
        self.assertEqual(len(ansi.COLORS_16), 16)
        self.assertEqual(len(ansi.BG_COLORS_256), 256)
        self.assertEqual(len(ansi.COLORS_256), 256)

        # Print the ANSI text attributes.
        print(f"ANSI text attributes")

        for index, attribute in enumerate(ansi.TEXT_ATTRIBUTES):
            print(f"[{index:>3}]: {attribute}The quick brown fox jumps over the lazy dog{ansi.RESET}")

        print()

        # Print the ANSI 16-colors to the terminal.
        print(f"ANSI 16-color palette")

        for index, (fg_color, bg_color) in enumerate(zip(ansi.COLORS_16, ansi.BG_COLORS_16)):
            print(
                f"[{index:>3}]: {fg_color}The quick brown fox jumps{ansi.RESET} {bg_color}over the lazy dog{ansi.RESET}")

        print()

        # Print the ANSI 256-colors to the terminal.
        print("ANSI 256-color palette (xterm-compatible)")

        for index, (fg_color, bg_color) in enumerate(zip(ansi.COLORS_256, ansi.BG_COLORS_256)):
            print(
                f"[{index:>3}]: {fg_color}The quick brown fox jumps{ansi.RESET} {bg_color}over the lazy dog{ansi.RESET}")
