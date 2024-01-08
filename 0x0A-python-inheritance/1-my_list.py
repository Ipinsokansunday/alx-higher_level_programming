#!/usr/bin/python3
"""Module with class MyList"""
class MyList(list):
    """Custom list class that inherits from the built-in list class."""


    def print_sorted(self):
        """Print the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
