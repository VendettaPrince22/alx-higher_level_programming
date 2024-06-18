#!/usr/bin/python3
"""Contains the function `read_file`"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout
    Args:
        filename (str): file to open
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
