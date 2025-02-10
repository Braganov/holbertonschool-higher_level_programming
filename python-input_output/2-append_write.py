#!/usr/bin/python3
""" defining append_write function """


def write_file(filename="", text=""):
    """ append a string to a text file (UTF8) and returns the number of characters written """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
