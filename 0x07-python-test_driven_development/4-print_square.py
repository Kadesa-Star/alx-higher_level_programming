#!/usr/bin/python3
"""function that prints a square using #"""


def print_square(size):
    """
    prints a square with the character #

    Args:
        size (int): the size length of the square.

    Raises:
        TypeError: is size is not an int or size is less than 0
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        print('#' * size)
