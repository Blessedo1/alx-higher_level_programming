#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        length = 0
        first = None
    elif sentence:
        length = len(sentence)
        first = sentence[0]
    return(length, first)
