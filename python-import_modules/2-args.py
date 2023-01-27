#!/usr/bin/python3
import sys
def argument():
    argc = len(sys.argv) - 1

    if argc == 0:
        print("{:d} arguments." .format(argc))

    elif argc == 1:
        print("{:d} argument:" .format(argc))
        print("{:d}: {}" .format(argc, sys.argv[1]))

    else:
        print("{:d} argument:" .format(argc))
        for num in range(1, argc + 1):
            print("{:d}: {}" .format(num, sys.argv[num]))

if __name__ == "__main__":

    argument()
