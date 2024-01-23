#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    maxi_val = my_list[0]

    for number in my_list:
        if number > maxi_val:
            maxi_val = number
        return (maxi_val)
