#!/usr/bin/python3
from add_0 import add
a = 1
b = 2
sum = add(a, b)
print("{:d} + {:d} = {:d}".format(a, b, sum))
if __name__ == "__main__":
    add(a, b)
