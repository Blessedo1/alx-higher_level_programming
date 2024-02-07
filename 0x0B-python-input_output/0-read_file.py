#!/usr/bin/python3
def read_file(filename=""):
    """reads a text file in UTF8 and prints to stdout"""
    with open(filename, mode='r', encoding='UTF8') as f:
        print(f.read(), end='')
