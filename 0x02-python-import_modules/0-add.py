#!/usr/bin/python3
from add_0 import add


def zero_add():
    a = 1
    b = 2
    total = add(a, b)
    print(f'{a} + {b} = {total}')


if __name__ == "__main__":
    zero_add()
