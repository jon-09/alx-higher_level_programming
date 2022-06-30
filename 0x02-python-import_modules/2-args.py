#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    argcnt = len(sys.argv) - 1
    if argcnt == 1:
        print("{} argument".format(argcnt), end="")
    else:
        print("{} arguments".format(argcnt), end="")
    if argcnt == 0:
        print(".")
    else:
        print(":")
    for i in range(1, argcnt):
        print("{}: {}".format(i, argcnt[i]))
    
