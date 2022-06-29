#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ord_val = ord(i)
        if ord_val >= 97 and ord_val <= 122:
            ord_val -= 32
        print("{:s}".format(chr(ord_val)), end='')
    print()
