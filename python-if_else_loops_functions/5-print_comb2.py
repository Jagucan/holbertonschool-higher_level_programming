#!/usr/bin/python3
n = []
for num in range(100):
    if num < 99:
        n.append("{:02}".format(num))
    if num == 99:
        n.append(str(num))
print(", ".join(n))