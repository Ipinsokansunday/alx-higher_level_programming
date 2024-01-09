#!/usr/bin/python3
""" a function that creates an Object from a “JSON file”"""


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object created from the JSON file.
    """
    import json

    with open(filename, 'r') as file:
        return json.load(file)
