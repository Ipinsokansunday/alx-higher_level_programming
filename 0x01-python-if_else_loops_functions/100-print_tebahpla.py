#!/usr/bin/python3
for x in range(122, 96, -1):
    if x % 2 == 0:
        n = chr(x)
    else:
        n = chr(x-32)
    print("{}".format(n), end="")
