#!/bin/python3
# contain the function find_peak

def find_peak(list_of_integers):
    """find the peak of a list of unsorted int"""
    lenght = len(list_of_integers)
    if lenght == 0:
        return None
    elif lenght == 1:
        return list_of_integers[0]
    else:
        i = 1
        while i < lenght - 1:
            if list_of_integers[i] > list_of_integers[i+1]:
                if list_of_integers[i] > list_of_integers[i-1]:
                    return list_of_integers[i]
            i +=1
        return list_of_integers[lenght - 1]
