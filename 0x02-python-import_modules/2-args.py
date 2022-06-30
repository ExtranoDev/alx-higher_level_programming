#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_arg = len(sys.argv) - 1
    str_arg = "arguments"
    if len_arg == 0:
        print("0 {}.".format(str_arg))
    elif len_arg > 0:
        print("{:d} {}:".format(len_arg, "argument" if len_arg == 1 else str_arg))
        count = 0
        for i in sys.argv:
            if i == sys.argv[0]:
                continue
            count = count + 1
            print("{:d}: {:s}".format(count, sys.argv[count]))
