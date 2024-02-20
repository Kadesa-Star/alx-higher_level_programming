#!/usr/bin/python3
""" reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """ reads a text file and prints to 1"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end='')
