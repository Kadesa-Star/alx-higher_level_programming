#!/usr/bin/python3
"""function that adds a new attribute to an object if possible"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.

    Raises:
        TypeError: If the attribute cannot be added
        """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
