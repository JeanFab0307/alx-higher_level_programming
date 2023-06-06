#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
remainder = number % 10

if number < 0:
    remainder = remainder - 10

print(f"Last digit of {number} is {remainder} and", end=" ")

if remainder > 5:
    print("is greater than 5")
elif remainder < 6 and remainder != 0:
    print("is less than 6 and not 0")
else:
    print("is 0")
