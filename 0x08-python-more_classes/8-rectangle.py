#!/usr/bin/python3
"""Rectangle module for ALX Python project 0x08 task 8."""

class Rectangle:
    """Class that defines a rectangle.

    Attributes:
        number_of_instances (int): Counter incrementing for every
            instantiation and decrementing for every instance deletion.
        print_symbol (str): Single character used in assembling string
            representation of rectangle.

    Methods:
        __init__(self, width=0, height=0): Initializes a Rectangle instance.
        area(self): Returns the area of the rectangle.
        perimeter(self): Returns the perimeter of the rectangle.
        _draw_rectangle(self): Formats a string to print the rectangle.
        __str__(self): Returns a string representation for printing.
        __repr__(self): Returns a string representation for eval().
        __del__(self): Decrements number_of_instances and prints a message.
        bigger_or_equal(rect_1, rect_2): Returns the bigger rectangle.

    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int): Horizontal dimension of the rectangle, defaults to 0.
            height (int): Vertical dimension of the rectangle, defaults to 0.

        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value: int):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self) -> int:
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value: int):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self) -> int:
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self) -> int:
        """Return the perimeter of the rectangle."""
        return 0 if self.__width == 0 or self.__height == 0 else 2 * (self.__width + self.__height)

    def _draw_rectangle(self) -> str:
        """Return a string representation of the rectangle."""
        result = ""
        for row in range(self.__height):
            result += str(self.print_symbol) * self.__width
            if self.__width != 0 and row < (self.__height - 1):
                result += '\n'
        return result

    def __str__(self) -> str:
        """Return a string representation for printing."""
        return self._draw_rectangle()

    def __repr__(self) -> str:
        """Return a string representation for eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Decrement number_of_instances and print a message."""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two instances and returns the larger of the two.

        Args:
            rect_1 (Rectangle): First instance to be compared.
            rect_2 (Rectangle): Second instance to be compared.

        Raises:
            TypeError: If `rect_1` or `rect_2` is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the larger area.
            If both rectangles have the same area, returns `rect_1`.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

