#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for j in range(list_length):
        try:
            div = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("Wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        else:
            new_list.append(div)
    return (new_list)
