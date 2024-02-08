#!/usr/bin/python3
"""define a class square"""


class Square:
    """a class square that defines  as square based on 0-square.py"""

    def __init__(self, size=0, position=(0, 0)):
        """this initializes a square with given size.


        Args:
            size (int): size of the square
            position (int, int): the position of the new square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the positon of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.


        Args:
            value (tuple): the position of the square

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
            ValueError: If postion contains non positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(m, int) for m in value) or
                any(m < 0 for m in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square withthe character #."""
        if self.__size == 0:
            print()
            return

        for m in range(self.__position[1]):
            print()

        for m in range(self.__size):
            for m in range(self.__position[0]):
                print(" ", end="")

            for m in range(self.__size):
                print("#", end="")

            print("")
