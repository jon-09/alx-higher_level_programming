#!/usr/bin/python3

def weight_average(my_list=[]):

    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    score = 0
    wght = 0

    for tup in my_list:
        score += (tup[0] * tup[1])
        wght += tup[1]

    return (score / wght)
