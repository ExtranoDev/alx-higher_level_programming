#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    len_arg = len(sys.argv)
    out_print = "{:d} {} {:d} = {:d}"
    if len_arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ops = sys.argv[2]
    if ops == "+":
        print(out_print.format(a, "+", b, add(a, b)))
        sys.exit(0)
    elif ops == "-":
        print(out_print.format(a, "-", b, sub(a, b)))
        sys.exit(0)
    elif ops == "*":
        passprint(out_print.format(a, "*", b, mul(a, b)))
        sys.exit(0)
    elif ops == "/":
        passprint(out_print.format(a, "/", b, div(a, b)))
        sys.exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)