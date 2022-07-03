#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return []
    return [not(bool(i % 2)) for i in my_list]
