#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if idx < 0:
        return(my_list)
    else:
        if my_list != 0:
            for new_list in my_list:
                new_list = my_list[:]
                new_list[idx] = element
                return(new_list)
