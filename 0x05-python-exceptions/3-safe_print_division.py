#!/usr/bin/python3


def safe_print_division(a, b):
    """Divides 2 integers and prints the result
    Args:
        a - integer 1
        b - integer 2
    Returns divided number
    """
    try:
        div = a / b
        return div
    except ZeroDivisionError:
        div = None
        return div
    finally:
        print("Inside result: {}".format(div))
