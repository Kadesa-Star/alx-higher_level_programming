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

    def __eq__(self, other):
        """check if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """check if two squares have different areas"""
        return self.area() != other.area()

    def __gt__(self, other):
        """check if area is greater than the other"""
        return self.area() > other.area()

    def __ge__(self, other):
        """check if area are greater or equal"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """check if the area of the first square is less than the second"""
        return self.area() < other.area()

    def __le__(self, other):
        """check if the area of the first square is less or equal to other"""
        return self.area() <= other.area()
