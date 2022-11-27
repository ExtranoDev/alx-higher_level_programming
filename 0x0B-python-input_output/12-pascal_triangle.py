#!/usr/bin/python3
"""
"""


def pascal_triangle(n):
    """
    """
    if n != 0:
        tri = []
        for i in range(n):
            temp_list = []
            for x in range(i + 1):
                if x == 0 or x == 1:
                    temp_list.append(1)
                else:
                    temp_list.append(tri[i-1][x-1] + tri[i-1][x])
            tri.append(temp_list)


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
