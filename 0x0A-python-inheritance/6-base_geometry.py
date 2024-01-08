#!/usr/bin/python3
"""programme with class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Method for calculating area."""
        raise NotImplementedError("area() is not implemented")
