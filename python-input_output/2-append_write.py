#!/usr/bin/python3
""" Appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """ Appends a string in a text file """

    with open(filename, mode="a", encoding="UTF-8") as my_file:
        num = my_file.write(text)
        return num
