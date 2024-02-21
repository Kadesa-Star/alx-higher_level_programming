#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        dictionary representation of the Student

        Args:
            attrs (list of str, optional): A list of attribute names
        """
        if (type(attrs) == list and
                all (type(elem) is str for elem in attrs)):
            return {k: getattr(self, k) for k in
                    attrs if hasattr(self, k)}
        return self.__dict__
