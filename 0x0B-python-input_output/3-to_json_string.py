#!/usr/bin/python3
"""Contains the `to_json_string` function"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)
    Args:
        my_obj (obj): object to convert
    Return:
        JSON representation; string
    """
    import json
    return json.dumps(my_obj)
