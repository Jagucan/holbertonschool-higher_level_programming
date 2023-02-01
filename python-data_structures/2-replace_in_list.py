#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    if idx < 0:
        return(my_list)
    else:
        if my_list != 0:
            my_list[idx] = element
            return(my_list)
