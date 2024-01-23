#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)

    maxi_val = my_list[0]

    for number in my_list:
        if number > maxi_value:
            maxi_value = number

    return (maxi_value)
