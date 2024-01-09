#!/usr/bin/python3
"""a function that returns an object (Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """Returns a Python data structure represented by a JSON string

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The Python data structure represented
        by the JSON string
    """
    import json

    return json.loads(my_str)
