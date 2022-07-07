#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tempList = [i for i, j in a_dictionary.items() if j == value]
    for i in tempList:
        a_dictionary.pop(i)
    return a_dictionary
