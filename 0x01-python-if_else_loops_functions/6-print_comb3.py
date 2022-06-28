#!/usr/bin/python3
for i in range(8):
    for j in range(10):
        if i != j:
            if j + (i * 10) < i + (j * 10):
                print("{:d}{:d}".format(i, j), end=", ")
print("{}".format(89))
