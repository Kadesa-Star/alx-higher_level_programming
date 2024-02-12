#!/usr/bin/python3
"""a class rectangle """


class Rectangle:
    """ a class representing a rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initializing an instance """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """string representation of rectangle"""
        if self.width == 0 or self.height == 0:
            return ''
        rectangle_str = ''
        for n in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + '\n'
        return rectangle_str.rstrip()

    def __repr__(self):
        """a string rep of rect for recreation using eval"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """deleting an instance of a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """method returns biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            rect_2
