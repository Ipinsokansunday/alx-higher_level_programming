#!/usr/bin/python3
"""programme with class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Method for calculating area."""
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validating an integer value."""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
