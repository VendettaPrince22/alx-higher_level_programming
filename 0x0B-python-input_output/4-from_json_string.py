#!/usr/bin/python3
"""Contain the `from_json_string` function"""


def from_json_string(my_str):
    """Returns an object represented by a JSON string
    Args:
        my_str (JSON): JSON string to convert
    Returns:
        obj
    """
    import json

    return json.loads(my_str)
