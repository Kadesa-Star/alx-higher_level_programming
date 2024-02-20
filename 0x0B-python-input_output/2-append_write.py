#!/usr/bin/python3
"""append a string to atextfile """


def append_write(filename="", text=""):
    """returns the number of characters written:"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
