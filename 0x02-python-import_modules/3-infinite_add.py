#!/usr/bin/python3
import sys


def add_arguments(arguments):
    result = sum(int(arg) for arg in arguments)
    return result


if __name__ == "__main__":
    arguments = sys.argv[1:]

    if not arguments:
        print(0)
    else:
        result = add_arguments(arguments)
        print(result)
