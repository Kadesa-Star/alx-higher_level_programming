#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for number in my_list:
        if type(number) == int:
            print("{}".format(number))
