#!/usr/bin/python3
"""
Class Square that defines a square by:
- Private instance attribute: size
- Property def size(self): to retrieve it
- Property setter def size(self, value): to set it:
  - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
  - if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Private instance attribute: position
- Property def position(self): to retrieve it
- Property setter def position(self, value): to set it:
  - position must be a tuple of 2 positive integers, otherwise raise a
  - TypeError exception with the message position must be a tuple of 2 positive integers
- Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0))
- Public instance method: def area(self): that returns the current square area
- Public instance method: def my_print(self): that prints in stdout the square with the character #:
  - if size is equal to 0, print an empty line
  - position should be used by using space
- Printing a Square instance should have the same behavior as my_print()
"""
class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
