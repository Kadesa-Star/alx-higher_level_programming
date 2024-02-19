#!/usr/bin/python3
""" defines an function that checks an inherites class """


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance a class that
    (directly or indirectly) from the specified class.


    Args:
        obj: The object to be checked
        a_class: The class to compare against

    Returns:
        True if the object is an instance of a clasd
        False otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    else:
        return False
