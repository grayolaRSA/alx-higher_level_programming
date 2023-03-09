#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    calc_add = add(a, b)
    calc_sub = sub(a, b)
    calc_mul = mul(a, b)
    calc_div = div(a, b)
    print(f'{a} + {b} = {calc_add}')
    print('{0} - {1} = {2}'.format(a, b, calc_sub))
    print('{0} * {1} = {2}'.format(a, b, calc_mul))
    print('{0} / {1} = {2}'.format(a, b, calc_div))
