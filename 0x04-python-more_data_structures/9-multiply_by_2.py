#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    b_dict = a_dictionary.copy()
    key_list = list(b_dict.keys())
    for key in key_list:
        b_dict[key] *= 2
    return b_dict
