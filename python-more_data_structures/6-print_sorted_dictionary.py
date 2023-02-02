#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_ordered = sorted(a_dictionary)
    for key in key_ordered:
        print (key, a_dictionary[key])