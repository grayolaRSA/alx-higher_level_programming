#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        ch = chr(ord(ch) - 32) if 97 <= ord(ch) <= 122 else ch
        print("{:s}".format(ch), end='')
    print('\n', end='')
