#!/usr/bin/python3

def uniq_add(my_list=[]):
    a = set(my_list)
    result = 0
    for i in a:
        result += i
    return result
