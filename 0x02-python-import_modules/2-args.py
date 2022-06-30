#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_arg = len(sys.argv)
    if len_arg == 1:
        print("0 arguments.")
    elif len_arg > 1:
        print("{:d} argument:".format(len_arg - 1))
        count = 0
        for i in sys.argv:
            if i == sys.argv[0]:
                continue
            count = count + 1
            print("{:d}: {:s}".format(count, sys.argv[count]))
