#!/usr/bin/python3
"""writes a string to atextfile """


def write_file(filename="", text=""):
    """returns the number of characters written:"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
