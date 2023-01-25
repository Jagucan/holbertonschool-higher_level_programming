#!/usr/bin/env python3
def uppercase(str):
    upper = ""
    
    for let in str:
        if ord(let) in range(97, 123):
            upper += chr(ord(let) - 32)
        else:
            upper += let
    print(upper)
