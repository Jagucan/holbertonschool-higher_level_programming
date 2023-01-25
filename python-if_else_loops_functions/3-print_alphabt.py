#!/usr/bin/python3
for len in range(97, 123):
    if chr(len) not in ["q", "e"]:
        print("{:s}".format(chr(len)), end="")
