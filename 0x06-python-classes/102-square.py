#!/usr/bin/python3
"""
Class Square that defines a square by:
- Private instance attribute: size
- Property def size(self): to retrieve it
- Property setter def size(self, value): to set it:
  - size must be a number (float or integer), otherwise raise
  - a TypeError exception with the message size must be a number
  - if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Instantiation with size: def __init__(self, size=0)
- Public instance method: def area(self): that returns the current square area
- Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area
"""

class Square:
    """Class Square that defines a square."""

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (float or int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the value of size.

        Returns:
        - float or int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method for setting the value of size.

        Parameters:
        - value (float or int): The size value to be set.

        Raises:
        - TypeError: If size is not a number (float or integer).
        - ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes and returns the current square area.

        Returns:
        - float or int: The area of the square.
        """
        return (self.__size ** 2)

    def __eq__(self, other):
        """
        Equality comparator based on square area.

        Returns:
        - bool: True if areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return (self.area() == other.area())
        return (False)

    def __ne__(self, other):
        """
        Inequality comparator based on square area.

        Returns:
        - bool: True if areas are not equal, False otherwise.
        """
        return(not self.__eq__(other))

    def __gt__(self, other):
        """
        Greater than comparator based on square area.

        Returns:
        - bool: True if the area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return (self.area() > other.area())
        return (False)

    def __ge__(self, other):
        """
        Greater than or equal comparator based on square area.

        Returns:
        - bool: True if the area is greater or equal, False otherwise.
        """
        return (self.__gt__(other) or self.__eq__(other))

    def __lt__(self, other):
        """
        Less than comparator based on square area.

        Returns:
        - bool: True if the area is less, False otherwise.
        """
        if isinstance(other, Square):
            return (self.area() < other.area())
        return (False)

    def __le__(self, other):
        """
        Less than or equal comparator based on square area.

        Returns:
        - bool: True if the area is less or equal, False otherwise.
        """
        return (self.__lt__(other) or self.__eq__(other))
