#!/usr/bin/python3
"""
This module hold a function to add 2 variables that are either 
be integers or floats
"""


def add_integer(a, b=98):
    """
    This function adds 2 elements
    Paramethers:
        a (float, int): The first value
        b (float, int): The second value. Defaults to 98.
    Errors:
        TypeError: if a is not a float or an int
        TypeError: if b is not a float or an int
    Returns:
        Integer with the addition of a and b
    """
    
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an int or float")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an int or float")
    else:
        if type(a) == float:
            a = int(a)
        if type(b) == float:
            b = int(b)
        return (a + b)
