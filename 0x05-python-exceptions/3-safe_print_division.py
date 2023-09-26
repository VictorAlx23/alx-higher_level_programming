#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Returns the division of a by b.

    Args:
        a (float or int): The numerator.
        b (float or int): The denominator.

    Returns:
        The result of the division or None if a TypeError or ZeroDivisionError occurs.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div

