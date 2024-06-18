#!/usr/bin/python3
"""Contains the `load_from_json_file` function"""


def load_from_json_file(filename):
    """Creates an object from a json file
    Args:
        filename (str): name of file retrieve item
    Returns:
        obj
    """
    import json
    with open(filename, 'r', encoding="utf-8") as f:
        d = json.load(f)
        return d
