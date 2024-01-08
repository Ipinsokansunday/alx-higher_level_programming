#!/usr/bin/python3
"""Module with class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): Size of the square.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with a given size.

        Args:
            size (int): The size of the square. Must be a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
