#!/usr/bin/python3


nc = 0
for n in range(122, 96, -1):
    if n % 2 == 0:
        nc = n
    else:
        nc = n - 32
    print("{}".format(chr(nc)), end='')
