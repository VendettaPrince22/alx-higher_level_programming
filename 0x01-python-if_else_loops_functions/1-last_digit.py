#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10

if number < 0:
    last_d = -last
else:
    last_d = last

if last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif last_d == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
elif last_d < 6 and last != 0:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")