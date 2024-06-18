#!/usr/bin/python3
"""Contains the `class_to_json` function"""


def class_to_json(obj):
    """Returns the dictionary description with simple ds for 
    JSON serialization of an object
    Args:
        obj: instance of a Class
    Returns:
        dict description
    """
    import json
    d = json.dumps(obj.__dict__)
    return d
