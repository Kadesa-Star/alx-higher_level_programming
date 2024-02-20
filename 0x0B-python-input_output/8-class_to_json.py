#!/usr/bin/python3
"""dictionary description of object with serializable attributes:"""


def class_to_json(obj):
    """dict description of an object suitable for JSON serialization"""
    return obj.__dict__
