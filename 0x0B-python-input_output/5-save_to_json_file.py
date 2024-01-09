#!/usr/bin/python3
"""a function that writes an Object to a text file,
using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation

    Args:
        my_obj: The Python object to be serialized and saved.
        filename (str): The name of the file
        to save the JSON representation.

    Returns:
        None
    """
    import json

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
