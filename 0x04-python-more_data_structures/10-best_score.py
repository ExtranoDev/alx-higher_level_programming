#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxi, name = 0, ""
        for i, j in a_dictionary.items():
            if j > maxi:
                maxi = j
                name = i
        return name
    return None
