#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = -(abs(number) % 10) if number < 0 else number % 10
print(f'Last digit of {number} is {last_digit}', end=' ')
if abs(last_digit) > 5:
    print('and is greater than 5')
elif abs(last_digit) < 6 and abs(last_digit) > 0:
    print('and is less than 6 and not 0')
else:
    print('and is 0')
