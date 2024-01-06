#!/usr/bin/python3
"""9-rectangle, ALX task on Python project 0x08 task 9.
"""


class Rectangle:
    """Class for printing or computation of dimensions of a rectangle.

    Takes in args for width and height of a rectangle and contains methods
    for calculation of the area or perimeter, and for creating a square by
    making a new instance of equal sides. __str__, __repr__, and __del__
    functionality defined below.

    Attributes:
        number_of_instances (int): Counter incrementing for every
            instantiation and decrementing for every instance deletion.
        print_symbol (str): Single character to be used in assembling a string
            representation of the rectangle.

    Methods:
        __init__(self, width=0, height=0): Initializes a Rectangle instance.
        area(self): Returns the area of the rectangle.
        perimeter(self): Returns the perimeter of the rectangle.
        _draw_rectangle(self): Formats a string of '#' and '\n' chars to print the rectangle.
        __str__(self): Returns a string representation for printing.
        __repr__(self): Returns a string representation for eval().
        __del__(self): Decrements number_of_instances and prints a message.
        bigger_or_equal(rect_1, rect_2): Returns the bigger rectangle.
        square(cls, size=0): Returns an instance with equal sides of length `size`.

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
        # attribute assignment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width.

        Args:
            value (int): Horizontal dimension of the rectangle.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height.

        Args:
            value (int): Vertical dimension of the rectangle.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 0 if self.__width == 0 or self.__height == 0 else 2 * (self.__width + self.__height)

    def _draw_rectangle(self):
        """Return a string representation of the rectangle."""
        result = ""
        for row in range(self.__height):
            result += str(self.print_symbol) * self.__width
            if self.__width != 0 and row < (self.__height - 1):
                result += '\n'
        return result

    def __str__(self):
        """Return a string representation for printing."""
        return self._draw_rectangle()

    def __repr__(self):
        """Return a string representation for eval()."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """Decrement number_of_instances and print a message upon
        deletion of instance."""
        cls.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two instances and returns the larger of the two.

        Args:
            rect_1 (Rectangle): First instance to be compared.
            rect_2 (Rectangle): Second instance to be compared.

        Raises:
            TypeError: If `rect_1` or `rect_2` is not an instance of cls.

        Returns:
            Rectangle: The rectangle with the larger area.
            If both rectangles have the same area, returns `rect_1`.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Returns an instance with equal sides of length `size`.

        Args:
            size (int): Length of sides of the square, defaults to 0.

        Returns:
            Rectangle: New instance with equal sides.

        """
        return cls(size, size)
