#!/usr/bin/python3
def no_c(my_string):
    dict = {ord(char): None for char in "cC"}
    list_of_chars = my_string.translate(dict)
    return list_of_chars
