#!/usr/bin/python3
"""Module with a function add_attribute"""


def add_attribute(obj, name, value):
    """
    Add a new attribute to an object if possible.

    Args:
        obj: Object to which the attribute should be added.
        name (str): Name of the new attribute.
        value: Value of the new attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    can_add_attribute = hasattr(obj, '__dict__') or \
        (hasattr(obj, '__slots__') and name in obj.__slots__)

    if can_add_attribute:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
