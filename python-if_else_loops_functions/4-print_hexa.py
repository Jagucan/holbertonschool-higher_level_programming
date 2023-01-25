#!/usr/bin/python3
for num in range(100):
    if num <= 99:
        print("{:d} = {:s}".format(num, hex(num)))
    num = num + 1
