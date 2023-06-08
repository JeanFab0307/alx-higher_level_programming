#!/usr/bin/python3

import sys

if __name__ == "__main__":
    end_mess = "s" if len(sys.argv) != 2 else ""
    ponct = ":" if len(sys.argv) != 1 else "."
    print("{} argument{}{}".format(len(sys.argv) - 1, end_mess, ponct))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
