#!/usr/bin/python3
import sys

argv = sys.argv
if __name__ == "__main__":

    if len(argv) == 1:
        print("0")
    else:
        add = 0
        for i in range(1, len(argv)):
            add += int(argv[i])
        print(add)
