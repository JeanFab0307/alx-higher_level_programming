#!/usr/bin/python3
"""Function write_file(filename, text)"""


def write_file(filename="", text=""):
    """
    Writes a string file and returns the number of char written.
    Creates the files if it does not exist.
    Else overwrite the content of the file it it exists
Args:
    filename(str): the path of the file
    text(str): the content added to the file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
