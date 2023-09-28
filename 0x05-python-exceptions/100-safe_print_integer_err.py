#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """
    Prints an integer using "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        True if the value is successfully printed as an integer.
        False if a TypeError or ValueError occurs.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        error_message = "Exception: {}".format(e)
        print(error_message, file=sys.stderr)
        return False

