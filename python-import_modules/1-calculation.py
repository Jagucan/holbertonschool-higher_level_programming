#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == "__main__":
    calc_add = add(a, b)
    calc_sub = sub(a, b)
    calc_mul = mul(a, b)
    calc_div = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, calc_add))
    print("{:d} - {:d} = {:d}".format(a, b, calc_sub))
    print("{:d} * {:d} = {:d}".format(a, b, calc_mul))
    print("{:d} / {:d} = {:d}".format(a, b, calc_div))
