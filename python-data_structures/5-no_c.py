#!/usr/bin/python3
def no_c(my_string):
    not_c = ""

    if my_string is not None:
        for len in my_string:
            if len not in ["c", "C"]:
                not_c += len

        return("{}".format(not_c))
