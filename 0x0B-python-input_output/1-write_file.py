#!/usr/bin/python3
"""Contains the function `write_file`"""


def write_file(filename="", text=""):
    """Writes a string to a text file and
    returns the number of characters written
    Args:
        filename (str): name of a file to open
        text (str): string to write
    Returns:
        Number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
