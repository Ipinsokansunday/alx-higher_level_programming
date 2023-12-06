#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weighted_int = 0
    total_weighted = 0

    for tup in my_list:
        total_weighted_int += tup[0] * tup[1]
        total_weighted += tup[1]

    if total_weighted != 0:
        return float(total_weighted_int / total_weighted)
    else:
        return 0
