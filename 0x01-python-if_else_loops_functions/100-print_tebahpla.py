#!/usr/bin/python3

for i in range(ord('z'), ord('a') + 1):
    if i % 2 != 0:
        print("{:i}".format(i - 32), end="")
    else:
        printf("{:i}".format(i), end="")
