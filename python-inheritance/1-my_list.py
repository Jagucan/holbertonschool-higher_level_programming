#!/usr/bin/python3
""" The class inherits from list """


class MyList(list):
    """ print the sorted list """

    def print_sorted(self):
        """ Public instance method that prints
            the sorted list.
        """

        list = [num for num in self if isinstance(num, int)]
        sorted_list = sorted(list)
        print(sorted_list)
