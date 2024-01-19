#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    number_args = len(sys.argv) - 1

    if number_args == 0:
        print("0 arguments.")
    else:
        print("{} {}:".format(number_args, 'argument' if number_args == 1
              else 'arguments'), end='\n' if number_args == 1 else '.\n')

        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
