#!/usr/bin/python3
"""define a class square"""


class Square:
    """a class square that defines  as square based on 0-square.py"""

    def __init__(self, size=0):
        """this initializes a square with given size.


        Args:
            size (int): size of the square

        Raises:
            TypeError: whenever size is not int
            ValueError: whenever size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
