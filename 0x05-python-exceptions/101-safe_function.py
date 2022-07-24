#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    ex = None
    try:
        ex = fct(*args)
        return ex
    except Exception as msg:
        print("Exception: {}".format(msg), file=sys.stderr)
        return ex
