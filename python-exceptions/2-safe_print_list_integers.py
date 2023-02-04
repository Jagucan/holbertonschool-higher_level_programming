#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    count = 0
    while num < x:
        try:
            if isinstance(my_list[num], int):
                print("{:d}".format(my_list[num]), end="")
                count = count + 1
        except IndexError:
            raise Exception("Error: out of range")
        num = num + 1
    print("")
    return count
