#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0")
    elif len(argv) == 2:
        print("{}".format(argv[1]))
    else:
        sum = argv[1]
        for i in argv[2:]:
            sum = int(sum) + int(i)
            print("{}".format(sum))
