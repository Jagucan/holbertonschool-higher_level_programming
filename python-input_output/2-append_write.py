#!/usr/bin/python3
""" Appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """ Appends a string in a text file """

    with open(filename, mode="w", encoding="UTF-8") as my_file:
        my_file.seek(2, 0)
        num = my_file.write(text)
        return num
