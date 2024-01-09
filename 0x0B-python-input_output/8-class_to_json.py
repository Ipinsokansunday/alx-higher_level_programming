#!/usr/bin/python3
"""a function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean) for
JSON serialization of an object"""


def class_to_json(obj):
    """Returns a dictionary description for JSON
    serialization of an object

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary representation of the
        object for JSON serialization.
    """
    attributes = obj.__dict__

    serializable_dict = {}

    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value

    return serializable_dict
