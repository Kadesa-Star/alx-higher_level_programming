#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    number_args = len(argv) - 1

    if number_args == 0:
        print("0 arguments.")
    else:
        print("{} {}:".format(number_args, 'argument' if number_args == 1
              else 'arguments'), end='\n' if number_args == 1 else '.\n')

        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
