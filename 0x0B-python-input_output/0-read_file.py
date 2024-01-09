#!/usr/bin/python3


def read_file(filename):
    """Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    if not filename:
        print("Error: Please provide a valid filename.")
        return

    try:
        with open(filename, "r", encoding="UTF-8") as file:
            content = file.read()
            print(content, end="")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
