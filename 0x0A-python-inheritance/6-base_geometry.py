#!/usr/bin/python3
""" Define an base class BaseGeometry. """


class BaseGeometry:
    """ Represent base geometry. """

    def area(self):
        """Exception indicating area() method is not implemented.
        """

        raise Exception("area() is not implemented")
