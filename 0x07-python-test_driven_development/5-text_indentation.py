#!/usr/bin/python3
"""function that prints a text wit 2 new lines afte .,? and :"""


def text_indentation(text):
    """ print text with 2 new lines

    Args:
        text (str): the input text

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1

    while char < len(text):
        print(text[char], end="")
        if text[char] == '\n' or text[char] in '.?:':
            if text[char] in '.?:':
                print('\n')
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
