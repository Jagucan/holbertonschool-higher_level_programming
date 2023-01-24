#!/usr/bin/python3
len = 97
letter = ""

while len < 123:
    if chr(len):
        letter = letter + chr(len)
    len = len + 1
print("{:s}".format(letter))
