#!/usr/bin/python3
len = 97
letter = ""
while len < 123:
    if chr(len) and chr(len) not in ['q', 'p']:
        letter = letter + chr(len)
    len = len + 1
print(f"{letter}")
