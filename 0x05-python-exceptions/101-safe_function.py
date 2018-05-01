#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        err = "Exception: " + str(err) + "\n"
        sys.stderr.write(err)
        return None
