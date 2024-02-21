#!/usr/bin/python3
"""  inserts a line of text to a file, after each line
containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a
    specific string in a file.

    Args:
        filename (str): name of file to modify
        search_string (str): string to search for in each line
        new_string (str): line of text to insert after each
        text containing the search string
    """
    lines = ""
    with open(filename) as file:
        for line in file:
            lines += line
            if search_string in line:
                line += new_string
    with open(filename, 'w') as w:
        w.write(lines)
