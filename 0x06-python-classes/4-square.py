#!/usr/bin/python3
"""
Class Square that defines a square by:
- Private instance attribute: size
- Property def size(self): to retrieve it
- Property setter def size(self, value): to set it:
  - size must be an integer, otherwise raise a
  - TypeError exception with the message size must be an integer
  - if size is less than 0, raise a ValueError exception
  - with the message size must be >= 0
- Instantiation with optional size: def __init__(self, size=0)
- Public instance method: def area(self): that returns the current square area
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
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the value of size.

        Returns:
        - int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method for setting the value of size.

        Parameters:
        - value (int): The size value to be set.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes and returns the current square area.

        Returns:
        - int: The area of the square.
        """
        return (self.__size ** 2)


