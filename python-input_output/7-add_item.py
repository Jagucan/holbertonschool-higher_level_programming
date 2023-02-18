#!/usr/bin/python3
""" Adds all arguments to a Python list, and then save them to a file """


import sys
""" Import sys """

from os import path
""" Import PATH """

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
""" Import save_to_json_file to 5-save_to_json_file"""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
""" Import load_from_json_file to 6-load_from_json_file """


filename = "add_item.json"
""" Python list """

args = sys.argv[1:]
""" Arguments """

my_list = []
if path.exists(filename):
    my_list = load_from_json_file(filename)
my_list += args
save_to_json_file(my_list, filename)
