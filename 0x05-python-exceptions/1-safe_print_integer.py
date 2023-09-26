#!/usr/bin/python3

def safe_print_integer(value):
    """
    Print an integer using "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        True if the value is successfully printed as an integer.
        False if a TypeError or ValueError occurs.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False

