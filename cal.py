#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: cal.py
Author: Roth Earl
Version: 0.0.0
Description: A program to ... WORK IN PROGRESS.
License: GNU GPLv3
"""

import calendar
import datetime
from typing import Final

from cli import colors

# Define constants.
DEFAULT_DATETIME_FORMAT: Final[str] = "%a %b %-d %-I:%M%p"


def main() -> None:
    """
    The main function of the program.
    :return: None
    """
    today = datetime.date.today()

    # Printing the current datetime, including format, will be options: https://strftime.org/
    if True:  # --datetime
        print(datetime.datetime.now().strftime(DEFAULT_DATETIME_FORMAT), "\n")  # --datetime-format

    # Weekday start will be an option, either monday (m) or sunday (s)
    if True:  # --weekday-start
        calendar.setfirstweekday(calendar.SUNDAY)

    # Which to print will be an option.
    if True:  # --year
        print_year(today)
    else:
        print_month(today)


def print_month(today: datetime.date) -> None:
    """
    Prints the current month.
    :param today: The current date.
    :return: None
    """
    month = calendar.month(today.year, today.month).splitlines()

    # Print the year header and the days of the week.
    print(month[0])
    print(month[1])

    # Print the weeks highlighting the current day of the month.
    day = f"{today.day:>2}"
    found_day = False

    for week in month[2:]:
        if not found_day and day in week:
            week = week.replace(f"{day}", f"{colors.REVERSE}{day}{colors.RESET}")
            print(week)
            found_day = True
        else:
            print(week)


def print_year(today: datetime.date) -> None:
    """
    Prints the current year.
    :param today: The current date.
    :return: None
    """
    calendar_output = calendar.calendar(today.year).splitlines()
    month_name = calendar.month_name[today.month]

    # Print the year header.
    print(calendar_output[0])
    print()

    # Scan ahead to the current month.
    month_start = 2

    # Scan ahead will be an option.
    if True:
        for line in calendar_output[2:]:
            if month_name in line:
                break

            month_start += 1

    #
    day = today.day
    day_find_str = f"{day:>3}"
    day_padded = f"{day:>2}"
    found_day, found_month = False, False

    for line in calendar_output[month_start:]:
        if not found_month and month_name in line:
            line = line.replace(month_name, f"{colors.REVERSE}{month_name}{colors.RESET}")
            print(line)
            found_month = True
        elif not line and True:  # This will be an option.
            break
        else:
            if not found_day and found_month and day_find_str in line:
                line = line.replace(f"{day_padded}", f"{colors.REVERSE}{day_padded}{colors.RESET}")
                found_day = True
                # print(line[:20], line[21:25], line[26:46], line[47:51], line[52:])

            print(line)


if __name__ == "__main__":
    main()
