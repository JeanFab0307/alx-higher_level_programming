#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        number = "{:d}"
        print(number.format(i))
