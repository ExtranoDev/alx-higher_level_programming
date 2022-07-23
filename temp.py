#!/usr/bin/python3
def debb(n, /, e=10, pluser=1, *, mul=1):
    return [i*mul for i in range(n, e, pluser)]

print(debb(1, 12)) # calling in position
print(debb(1, 12, 2)) # calling in position
print(debb(1, 12, pluser=2)) # calling in position and keyword
print(debb(1, 20, 2, )) #

[print("{:d}".format(i), end=" ") for i in range(5)]

print("\n")
# *args -- list()
# **args -- dict()
def dan(a, *ife, **oji):
    [print(a, ":", i) for i in ife]
    [print(name, ":", value) for name, value in oji.items()]

dan(4, 5, 6, 7, 8, cohort=6, size=3000, name="Gritters", )
dan(4, 5, 6, 7, 8, 10, 11, 12, 13)

def funcmix(**args):
    return [(i, j) for i, j in args.items()]

print(funcmix(att=1, show=2, status="Sweet", how="Nice"))
