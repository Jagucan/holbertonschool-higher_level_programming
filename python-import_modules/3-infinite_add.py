#!/usr/bin/python3
import sys


def argument():

    argc = len(sys.argv) - 1
    sum = 0

    for num in range(1, argc + 1):
        sum += int(sys.argv[num])

    print("{:d}" .format(sum))


if __name__ == "__main__":
    argument()
