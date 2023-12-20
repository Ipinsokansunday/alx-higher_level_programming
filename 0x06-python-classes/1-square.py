#!/usr/bin/python3
"""
Class Square that defines a square by:
- Private instance attribute: size
- Instantiation with size (no type/value verification)
"""

class Square:
    """
    Class Square with private instance attribute size.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square.
        """
        self.__size = size
