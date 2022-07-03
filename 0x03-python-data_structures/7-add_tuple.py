#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a or tuple_b:
        temp = [tuple_a, tuple_b]
        idx = 0
        for i in temp:
            if len(i) < 2:
                if len(i) == 0:
                    temp[idx] = (0, 0)
                else:
                    temp[idx] = (temp[idx][0], 0)
            idx = idx + 1
        return (temp[0][0] + temp [1][0], temp[0][1] + temp[1][1])
            
            
