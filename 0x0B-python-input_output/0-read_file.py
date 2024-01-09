#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename):
    """Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
