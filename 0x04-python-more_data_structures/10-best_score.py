#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest_key = list(a_dictionary.keys())[0]
    biggest_value = a_dictionary[biggest_key]
    for i, j in a_dictionary.items():
        if j > biggest_value:
            biggest_value = j
            biggest_key = i
    return biggest_key
