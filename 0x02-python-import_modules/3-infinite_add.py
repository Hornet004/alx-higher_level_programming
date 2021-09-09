#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    val = 0
    for arg in argv[1:]:
        val += int(arg)
    print("{:d}".format(res))
