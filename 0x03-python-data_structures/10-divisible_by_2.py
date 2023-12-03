#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple_two = []
    for number in my_list:
        if (number % 2) == 0:
            multiple_two.append(True)
        else:
            multiple_two.append(False)
    return(multiple_two)
