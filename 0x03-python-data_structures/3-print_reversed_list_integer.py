#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for all_int in my_list:
            print("{:d}".format(all_int))
