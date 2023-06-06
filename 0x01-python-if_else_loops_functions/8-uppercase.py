#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        if ord(letter) <= ord('z') and ord(letter) >= ord('a'):
            letter = chr(ord(letter) - ord('a') + ord('A'))
        print("{}".format(letter), end="")

    print("")
