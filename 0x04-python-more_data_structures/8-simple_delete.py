#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    key_list = list(a_dictionary.keys())
    for dic_key in key_list:
        if dic_key == key:
            a_dictionary.pop(key)
            break
    return a_dictionary
