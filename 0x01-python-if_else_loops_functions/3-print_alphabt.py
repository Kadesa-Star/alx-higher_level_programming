#!/usr/bin/python3
for j in range(ord('a'), ord('z') + 1):
    if chr(j) != 'q' and chr(j) != 'e':
        print("{:c}".format(j), end='')
