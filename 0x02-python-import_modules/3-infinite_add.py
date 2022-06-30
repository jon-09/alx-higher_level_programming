#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    count = len(sys.argv)
    cnt = count - 1
    sm = 0

    if cnt == 0:
        print("0")
    elif cnt == 1:
        print("{}".format(sys.argv[i]))
    else:
        for i in range(1, count):
            sm += int(sys.argv[i])
        print("{}".format(sm))
