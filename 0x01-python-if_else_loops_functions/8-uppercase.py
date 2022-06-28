#!/usr/bin/python3

def uppercase(str):
    for c in str:
        ch = ord(c)
        if ch in range(ord('a'), ord('z') + 1):
            ch -= 32
        print("{:c}".format(ch), end="")
    print("")
