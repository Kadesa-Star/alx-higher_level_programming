#!/usr/bin/python3
""" defines returns True if object is an instance of a  class """


def is_kind_of_class(obj, a_class):
    """
    Check if an object is a class or inherited instance

    Args:
        obj (any): The object to be checked
        a_class: The class to compare against.

    Returns:
        True if the object is an instance
        False otherwise
    """

    if isinstance(obj, a_class):
        return True

    return False
