#!/usr/bin/python3
"""this is a LockedClass definition"""


class LockedClass:
    """
    Prevents the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """
    __slots__ = ["first_name"]
