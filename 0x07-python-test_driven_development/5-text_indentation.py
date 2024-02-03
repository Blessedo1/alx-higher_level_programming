#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise("text must be a string")
    for i in text:
        if i != ' ':
            print("{}".format(i), end='')
        if i == "." or i == "?" or i == ":":
            print()
            print()
    print()
