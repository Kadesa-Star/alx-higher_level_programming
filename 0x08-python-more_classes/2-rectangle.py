#!/usr/bin/python3
"""a class rectangle """


class Rectangle:
    """ a class representing a rectangle """

    def __init__(self, width=0, height=0):
        """ initializing an instance """

        self.width = width
        self.height = height

    @property
    def width(self):
        """getting rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getting height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate area"""
        return self.width * self.height

    def perimeter(self):
        """to calculate perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
