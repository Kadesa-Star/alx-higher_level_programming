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
    # open the file in read mode
    with open(filename, 'r') as file:
        lines = file.readlines()

    # open the file in write mod
    with open(filename, 'w') as file:
        #iterate over the lines
        for line in lines:
            #write the orginal line to the file
            file.write(line)
            #if search string is found append new string
            if search_string in line:
                file.write(new_string + '\n')
