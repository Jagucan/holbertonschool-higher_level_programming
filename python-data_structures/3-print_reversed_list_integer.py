#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    new_list = ""
    for num in my_list:
        new_list = str(num) + new_list
    print(str.format(new_list))

if __name__ == "__main__":
    print_reversed_list_integer(my_list=[])
