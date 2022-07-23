#!/usr/bin/python3
def safe_print_division(a, b):
    rt_res = None
    try:
        rt_res = a / b
        return (rt_res)
    except ZeroDivisionError:
        return (rt_res)
    finally:
        print("Inside result: {}".format(rt_res))

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
