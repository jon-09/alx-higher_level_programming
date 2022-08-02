#!/usr/bin/python3
""" A module for write function """


def write_file(filename="", text=""):
    """ A function that writes a string to a text file (UTF-8) and returns
    the number of characters written """

    with open(filename, encoding='UTF-8', mode='w') as ftext:
        return ftext.write(str(text))
