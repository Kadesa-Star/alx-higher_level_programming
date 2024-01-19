#!/usr/bin/python3

if __name__ == "__main__":
    """Print number of list of args."""
    import sys

    number_args = len(sys.argv) - 1

    if number_args == 0:
        print("0 arguments.")
    elif number_args == 1:
        print("1 argument.")
    else:
        print("{} arguments:".format(number_args))
    for j in range(number_args):
        print("{}: {}".format(j + 1, sys.argv[j + 1]))
