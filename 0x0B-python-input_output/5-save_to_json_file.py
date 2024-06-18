#!/usr/bin/python3
"""Contains the `save_to_json_file` function"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation
    Args:
        my_obj (obj): obj to write to file
        filename (str): name of the file to write to
    """
    import json
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
