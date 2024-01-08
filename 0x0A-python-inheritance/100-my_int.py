#!/usr/bin/python3
"""Module with a class MyInt"""


class MyInt(int):
    """Class that inherits from int"""

    def __init__(self, my_int):
        """Initialize a value my_int"""
        self.my_int = my_int

    @property
    def my_int(self):
        return self.__my_int

    @my_int.setter
    def my_int(self, my_int):
        if not isinstance(my_int, int):
            raise TypeError("my_int must be an integer")
        self.__my_int = my_int

    def __eq__(self, other):
        """Inverted equal method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted not equal method"""
        return super().__eq__(other)
