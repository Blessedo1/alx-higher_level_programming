#!/usr/bin/python3
for i in range(97, 123):
    while i != ord('e') and i != ord('q'):
        print("{:c}".format(i), end='')
        break
