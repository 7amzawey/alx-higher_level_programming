#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastdigi = abs(number) % 10
elif number < 0:
    last = abs(number) % 10
    lastdigi = -1 * last
if lastdigi > 5:
    print(f"Last digit of {number} is {lastdigi} and is greater than 5")
elif lastdigi == 0:
    print(f"Last digit of {number} is {lastdigi} and is 0")
else:
    print(f"Last digit of {number} is {lastdigi} and is less than 6 and not 0")
