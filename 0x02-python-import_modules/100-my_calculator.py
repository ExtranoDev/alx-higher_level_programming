#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    len_arg = len(sys.argv)

    if len_arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = sys.argv[2]
    if ops not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    out_print = "{:d} {} {:d} = {:d}"

    if ops == "+":
        print(out_print.format(a, "+", b, add(a, b)))
    elif ops == "-":
        print(out_print.format(a, "-", b, sub(a, b)))
    elif ops == "*":
        print(out_print.format(a, "*", b, mul(a, b)))
    elif ops == "/":
        print(out_print.format(a, "/", b, div(a, b)))
