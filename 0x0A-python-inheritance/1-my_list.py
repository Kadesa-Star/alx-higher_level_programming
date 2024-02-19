#!/usr/bin/python3
""" this is a class that inherists from list"""


class MyList(list):
"""this class inherits from list"""

    def print_sorted(self):
        """
        prints the list in sorted manner (ascending)
        """
        sorted_list = sorted(self)
        print(sorted_list)
