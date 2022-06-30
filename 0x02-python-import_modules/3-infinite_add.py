#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_arg = len(sys.argv)
    sum_arg = 0
    if len_arg == 1:
        pass
    elif len_arg > 1:
        for i in sys.argv[1:]:
            sum_arg = sum_arg + int(i)
    print(sum_arg)
