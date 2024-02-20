#!/usr/bin/python3
""" Defines a function that checks for a class."""


def is_same_class(obj, a_class):
    """
    check if an object is exactly an instance of a given class

    Args:
        obj (any): The object to check
        a_class (type): The class to compare the object type to
    Returns:
        True if object is an instance of a_class
        False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
