#!/usr/bin/python3
"""define a magicclass matching a bytecode"""


class MagicClass:
    """represent a circle"""

    def __init__(self, radius=0):
        """initializing a  MagicClass

        Arg:
            radius (float or int): the radius should be either integer or float
        Raises:
            TypeError: if radius is not float or integer
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calculating the area of the circle using the formula πr^2"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calculate and return the circumference of the circle using 2πr"""
        return 2 * math.pi * self.__radius
