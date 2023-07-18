#!/usr/bin/python3
"""Function read_file"""


def read_file(filename=""):
    """
    Read a textfile and prints to stdout
Arg:
    filename(str): the path of the file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read())
