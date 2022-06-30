#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    argcnt = len(sys.argv)
    argn = argcnt - 1
    if argcnt - 1 == 1:
        print("{} argument".format(argn), end="")
    else:
        print("{} arguments".format(argn), end="")
    if argcnt - 1 == 0:
        print(".")
    else:
        print(":")
    for i in range(1, argcnt):
        print("{}: {}".format(i, sys.argv[i]))
