#!/usr/bin/python3
for d in range(0, 10):
    for s in range(d + 1, 10):
        if d == 8 and s == 9:
            print('89')
        else:
            print("{}{}, ".format(d, s), end='')
