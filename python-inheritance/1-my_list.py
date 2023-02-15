#!/usr/bin/python3
""" The class inherits from list """


class MyList(list):
    """ print the sorted list """

    def print_sorted(self):
        """ Public instance method that prints
            the sorted list.
        """
        print(sorted(self))