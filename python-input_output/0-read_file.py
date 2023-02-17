#!/usr/bin/python3
""" _summary_ """


def read_file(filename=""):
    with open(filename, mode="r", encoding="UFT8") as my_file:
        content = my_file.read()
        print(content)