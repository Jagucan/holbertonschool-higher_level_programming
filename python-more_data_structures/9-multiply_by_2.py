#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult = \
        dict(map(lambda item:(item[0], item[1] * 2), a_dictionary.items()))
    return mult
