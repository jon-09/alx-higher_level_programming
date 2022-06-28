#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dg = number[-1:]
print(f"Last digit of {number:d} is {dg:d}", end=" ")
if dg > 5:
    print("and is greater than 5")
elif dg == 0:
    print("0")
elif dg < 6:
    print("and is less than 6 and not 0")
