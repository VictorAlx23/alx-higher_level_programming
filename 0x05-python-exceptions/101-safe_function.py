#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct: The function to execute.
        *args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        error_message = "Exception: {}".format(e)
        print(error_message, file=sys.stderr)
        return None

