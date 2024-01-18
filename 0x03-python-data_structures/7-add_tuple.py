#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l_a, l_b = len(tuple_a), len(tuple_b)
    ituple = (tuple_a[0] if l_a >= 1 else 0) + (tuple_b[0] if l_b >= 1 else 0)
    jtuple2 = (tuple_a[1] if l_a >= 2 else 0) + (tuple_b[1] if l_b >= 2 else 0)
    return (ituple, jtuple2)
