#!/usr/bin/python3
"""COntains function append_write"""


def append_write(filename="", text=""):
    """Append a str to a textfile
Args:
    filename(str): the file pathname
    text(str): the string to append
Return:
    The number of character added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        num_char = f.write(text)
        return num_char
