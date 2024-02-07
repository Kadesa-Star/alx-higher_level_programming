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
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square.

        Args: value (int): the size of the square

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square withthe character #."""
        if self.__size == 0:
            print()
            return

        for m in range(self.__size):
            print("#" * self.__size)
