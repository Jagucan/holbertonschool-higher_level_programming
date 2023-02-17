#!/usr/bin/python3
""" Reads a text file (UTF8) and prints
    it to stdout using with.
"""


def read_file(filename=""):
    """ Read an file """

    with open(filename, mode="r", encoding="UTF-8") as my_file:
        for content in my_file:
            print(content, end="")
