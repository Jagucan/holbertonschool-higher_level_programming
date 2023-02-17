#!/usr/bin/python3
""" Writes a string to a text file (UTF8) and return
    the number of characters.
"""


def write_file(filename="", text=""):
    """ Writhe to a file """

    with open(filename, mode="w", encoding="UTF-8") as my_file:
        num = my_file.write(text)
        return num
