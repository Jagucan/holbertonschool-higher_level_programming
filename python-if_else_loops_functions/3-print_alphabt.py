#!/usr/bin/python3
letter = 97
while letter < 123:
    if chr(letter) and chr(letter) not in ["q", "e"]:
        print(chr(letter), end='')
    letter += 1
