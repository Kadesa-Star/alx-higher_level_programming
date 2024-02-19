#!/usr/bin/python3
""" Defines an function that checks an inherites clast. """


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance a class
    (directly or indirectly) from the specified class.


    Args:
        obj: The object to be checked
        a_class: The class to compare against

    Returns:
        True if the object is an instance of a clasd
        False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
