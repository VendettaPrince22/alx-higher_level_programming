#!/usr/bin/python3
"""Contains the `append_write` function"""


def append_write(filename="", text=""):
    """Appends a string and returns the number of characters added
    Args:
        filename (str): name of file to append to
        text (str): text to append to file
    Returns:
        Number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        append_data = f.write(text)
        return append_data
