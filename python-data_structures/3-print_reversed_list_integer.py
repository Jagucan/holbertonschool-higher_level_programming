#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if my_list is not None:
        for num in my_list[::-1]:
            if isinstance(num, int):
                print("{:d}".format(num))

            elif isinstance(num, str):
                print("Traceback (most recent call last):")
                break
