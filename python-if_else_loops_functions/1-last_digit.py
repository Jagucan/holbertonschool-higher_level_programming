#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num1 = number % 10
num2 = number % -10
if number > 0:
    if num1 > 5:
        print("Last digit of {:d} is {:d} and is greater than 5"
              .format(number, num1))
    elif num1 < 6:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0"
              .format(number, num1))
    else:
        print("Last digit of {:d} is {:d} and is zero"
              .format(number, num1))

elif number < 0:
    if num2 < 0 & num2 < 6:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0"
              .format(number, num2))
    elif num2 < 0 & num2 > 5:
        print("Last digit of {:d} is {:d} and is greater than 5"
              .format(number, num2))
    else:
        print("Last digit of {:d} is {:d} and is zero"
              .format(number, num2))

else:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, num2))
