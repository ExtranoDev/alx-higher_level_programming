#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_a = len(sys.argv) - 1
    str_a = "arguments"
    if len_a == 0:
        print("0 {}.".format(str_a))
    elif len_a > 0:
        print("{:d} {}:".format(len_a, "argument" if len_a == 1 else str_a))
        count = 0
        for i in sys.argv:
            if i == sys.argv[0]:
                continue
            count = count + 1
            print("{:d}: {:s}".format(count, sys.argv[count]))
