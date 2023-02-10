#!/usr/bin/python3
""" The function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ Prints a text whit identation """

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n\n", end="")
            i += 1

            while i < len(text) and text[i] == " ":
                i += 1

        else:
            i += 1
