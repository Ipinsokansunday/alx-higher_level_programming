#!/usr/bin/python3
"""
=============================
Module with the method lookup
=============================
"""

def lookup(obj):
    """
    Return a list of attributes and methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        list: A list containing the names of attributes and methods.
    """
    # Use dir() to get all attributes and methods
    all_names = dir(obj)

    # Filter out the ones that are not callable (methods)
    methods = [name for name in all_names if callable(getattr(obj, name))]

    return methods
