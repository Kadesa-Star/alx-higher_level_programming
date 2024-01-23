#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        maxi_val = my_list[0]
        for number in range(len(my_list)):
            if my_list[number] > maxi_value:
                maxi_value = my_list[number]
        return (maxi_value)
