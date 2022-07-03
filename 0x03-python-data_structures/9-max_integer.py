#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxi = 0
        for i in my_list:
            if i > maxi:
                maxi = i
        return maxi
    elif my_list == []:
        return None
