#!/usr/bin/python3


def safe_print_integer(value):
    """Prints an integer
    Args:
        value: number to print
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
