#!/usr/bin/python3
"""
Class Square that defines a square by:
- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0)
- Size must be an integer, otherwise raise a
- TypeError exception with the message size must be an integer
- If size is less than 0, raise a ValueError
- exception with the message size must be >= 0
"""

class Square:
    """
    Class Square with private instance attribute size.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square (default is 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
