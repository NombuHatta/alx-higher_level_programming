#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    num_args = len(argv)
    print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}", end='')

    print(":" if num_args > 0 else ".")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
