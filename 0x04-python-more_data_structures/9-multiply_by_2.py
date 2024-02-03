#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiples = a_dictionary.copy()
    for i, j in multiples.items():
        multiples[i] = j * 2
    return multiples
