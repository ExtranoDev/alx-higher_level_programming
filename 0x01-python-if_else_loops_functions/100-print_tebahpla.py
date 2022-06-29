#!/usr/bin/python3
num = 122
for i in range(26):
    print("{}".format(chr(num)), end="")
    if num >= 97 and num <= 122:
        num -= 33
    elif num >= 65 and num <= 90:
        num += 31
