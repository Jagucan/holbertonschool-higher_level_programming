#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = int(str(number)[-1])

if number > 0:
    if num > 5:
        print(f"Last digit of {number} is {num} and is greater than 5")
    elif num < 6:
        print(f"Last digit of {number} is {num} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {num} and is zero")
elif number < 0:
    if num > 0 & num < 6:
        print(f"Last digit of {number} is -{num} and is less than 6 and not 0")
    elif num < 0 & num > 5:
        print(f"Last digit of {number} is -{num} and is greater than 5")
    else:
        print(f"Last digit of {number} is {num} and is zero")
else:
    print(f"Last digit of {number} is {num} and is 0")
    