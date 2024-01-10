#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indentation_level = 0
    for char in text:
        print(char, end="")
        if char == "\n" or char in ".?:":
            if char in ".?:":
                print("\n")
                indentation_level = 0
            else:
                indentation_level = 1
        elif char == ' ' and indentation_level > 0:
            indentation_level += 1
        else:
            indentation_level = 0
