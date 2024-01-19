#!/usr/bin/python3

if __name__ = "__main__":
    """addition of args."""
    import sys

    summ = 0
    for j in range(len(sys.argv) - 1):
        summ += int(sys.argv[j + 1])
    print("{}".format(summ))
