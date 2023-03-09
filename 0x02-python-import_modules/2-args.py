#!/usr/bin/python3
import sys

argv_len = len(sys.argv)


print(f'{argv_len - 1}', end=' ')
if argv_len == 2:
    print("argument:")
elif argv_len > 2:
    print("arguments:")
else:
    print("argument.")

for arg in sys.argv[1:]:
    print(arg)

if __name__ == "__main__":
    pass
