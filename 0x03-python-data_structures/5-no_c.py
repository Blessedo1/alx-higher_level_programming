#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for i in range(len(my_string)):
        while my_string[i] != "c" and my_string[i] != "C":
            newstring = newstring + my_string[i]
            break
    return newstring
