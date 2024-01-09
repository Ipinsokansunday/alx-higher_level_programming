#!/usr/bin/python3
"""a script that adds all arguments to
a Python list, and then save them to a file"""


import json


def add_items_to_list_and_save(arguments):
    """Adds command-line arguments to a
    Python list and saves it as a JSON file.

    Args:
        arguments (list): List of command-line arguments.

    Returns:
        None
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
