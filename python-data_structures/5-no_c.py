#!/usr/bin/python3
def no_c(my_string):
    for len in my_string:
        if len not in ["c", "C"]:
            print("{}".format(len), end="")