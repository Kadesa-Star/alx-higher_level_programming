#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for r in range(x):
            value = my_list[r]
            if isinstance(value, int):
                print("{:d}".format(value), end='')
                count += 1
    except (IndexError, ValueError, TypeError):
        pass
    finally:
        print()
        return (count)
