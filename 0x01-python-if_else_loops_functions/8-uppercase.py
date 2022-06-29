#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ord_val = ord(i)
        print("{:s}".format((chr(ord_val - 32) if (ord_val >= \
                97) and (ord_val <= 122) else i)), end='')
    print()
