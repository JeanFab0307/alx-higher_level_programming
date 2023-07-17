#!/usr/bin/python3
"""
Contains the function text_indentation(text)
"""


def text_indentation(text):
    """
Prints 2 new line after the char '.' '?' ':'

Example:
    text_indentation("Hello. World")
    Hello.
    
    World

Args:
    text(str): must be string
"""
    if type(text) != str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text): 
        print(text[i], end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("\n")
            if i + 1 >= len(text):
                break
            while text[i + 1] == " ":
                i += 1
        i += 1



