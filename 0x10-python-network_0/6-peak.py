#!/usr/bin/python3
# function finds a peak in a list of unsorted integers

def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    arr = list_of_integers

    arr_len = len(arr) - 1

    if arr[0] >= arr[1]:
        return arr[0]
    if arr[arr_len] >= arr[arr_len - 1]:
        return arr[arr_len]

    for i in range(1, arr_len):
        if (arr[i] >= arr[i + 1] and arr[i] >= arr[i - 1]):
            return arr[i]
