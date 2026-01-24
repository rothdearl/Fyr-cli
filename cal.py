#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: cal.py
Author: Roth Earl
Version: 1.3.5
Description: A program to filter matching lines in files.
License: GNU GPLv3
"""

import calendar
import datetime
import re


def main() -> None:
    """
    The main function of the program.
    :return: None
    """
    today = datetime.date.today()

    calendar.setfirstweekday(calendar.SUNDAY)

    print(calendar.month(today.year, today.month))
    print(calendar.calendar(today.year))


def highlight_today():
    today = datetime.date.today()

    # ANSI escape sequences for inverse colors
    highlight_start = '\033[7m'
    highlight_end = '\033[0m'

    # Generate the calendar string with consistent spacing
    cal_output_consistent = calendar.month(today.year, today.month, w=2)

    # Format the current day with leading space or not depending on its value
    day_str_formatted = str(today.day).rjust(2)

    # Create the highlighted day string
    highlighted_day_str = f"{highlight_start}{day_str_formatted}{highlight_end}"

    # Use regex to find and replace the day, ensuring it's a whole number in the calendar
    # This helps avoid replacing a digit in the year.
    rday = r'(?<!\d)' + re.escape(str(today.day)) + r'(?!\d)'
    highlighted_calendar = re.sub(rday, highlighted_day_str, cal_output_consistent, count=1)

    print(highlighted_calendar)


def print_highlighted_year_calendar():
    """Prints the current year's calendar with today's date highlighted."""

    # Get today's date
    today = datetime.date.today()
    current_year = today.year
    current_day = today.day
    current_month = today.month

    # ANSI escape codes for highlighting (reverse video - swap foreground/background colors)
    # This works in most modern terminals and PowerShell/Windows Terminal
    HIGHLIGHT_START = "\033[7m"
    HIGHLIGHT_END = "\033[0m"

    # Generate the full year's calendar as a string
    # w=2: day width, l=1: lines per week, c=6: space between months, m=3: months per row
    cal = calendar.TextCalendar(calendar.MONDAY) # Start week on Monday
    year_calendar_str = cal.formatyear(current_year, w=2, l=1, c=6, m=3)

    # Prepare the string representation of today's day for replacement
    # Ensure consistent width (2 chars) to maintain calendar alignment
    day_str = str(current_day).rjust(2)
    highlighted_day_str = f"{HIGHLIGHT_START}{day_str}{HIGHLIGHT_END}"

    # Replace the current day in the calendar string.
    # The trickiest part is ensuring only the correct day is replaced in the correct month.
    # For a simple console output, direct replacement across the whole string will highlight
    # all occurrences of the day number. A more robust solution would involve month-by-month processing.

    # Below is a simple implementation that replaces the first occurrence of the day in the current month's section.
    # This might highlight other dates if they are identical in other months.
    # A complete solution is complex. Let's provide a function that iterates month by month for accuracy.
    for month in range(1, 13):
        month_cal_str = calendar.month(current_year, month)
        # Only replace in the current month
        if month == current_month:
            # Use regex with word boundaries (approximated) to avoid partial number matches (e.g., 2 in 20, 21, etc)
            # This is still not perfect as spacing in the calendar string is tricky.
            # The most reliable way is to iterate over the lines of the month string.

            # Recreate month_cal_str with consistent spacing for easier highlighting
            month_cal_list = calendar.month(current_year, month).splitlines()
            for i, line in enumerate(month_cal_list):
                # We are only interested in lines with day numbers (not header lines)
                if any(char.isdigit() for char in line) and len(line) > 10:
                    # Replace the exact day number with the highlighted version, matching the spacing
                    # This relies on fixed-width columns
                    line = re.sub(rf'\b{re.escape(day_str)}\b', highlighted_day_str, line)
                    month_cal_list[i] = line
            month_cal_str = "\n".join(month_cal_list)

        print(month_cal_str)
        print("-" * 20) # Separator between months


if __name__ == "__main__":
    main()
    highlight_today()
    #print_highlighted_year_calendar()
