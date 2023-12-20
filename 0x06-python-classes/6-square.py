
#!/usr/bin/python3
"""
Class Square that defines a square by:
- Private instance attribute: size
- Property def size(self): to retrieve it
- Property setter def size(self, value): to set it:
  - size must be an integer, otherwise raise a TypeError exception with
  - the message size must be an integer
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
  - position should be used by using space - Don’t fill lines by spaces when position[1] > 0
"""

class Square:
    """
    Class Square with private instance attributes size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square (default is 0).
        - position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

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

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter method for retrieving the value of position.

        Returns:
        - tuple: The position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Setter method for setting the value of position.

        Parameters:
        - value (tuple): The position value to be set.

        Raises:
        - TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Computes and returns the current square area.

        Returns:
        - int: The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints the square with the character # and using the position.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
