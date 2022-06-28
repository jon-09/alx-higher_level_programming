#!/usr/bin/python3
for nm1 in range(0, 10):
    for nm2 in range(nm1 + 1, 10):
        if nm1 == 8 and nm2 == 9:
            print("{}{}".format(nm1, nm2))
        else:
            print("{}{}".format(nm1, nm2), end=", ")
