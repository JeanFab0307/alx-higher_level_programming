#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    result = [0, 0]
    for i in range(len(tuple_a)):
        if i == 2:
            break
        result[i] = tuple_a[i]
    for i in range(len(tuple_b)):
        if i == 2:
            break
        result[i] += tuple_b[i]
    result = tuple(result)
    return result
