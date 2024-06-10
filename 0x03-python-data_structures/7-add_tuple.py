#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples
    Args:
        tuple_a: first tuple
        tuple_b: second tuple
    Returns a tuple
    """
    if len(tuple_a) < 2:
        if len(tuple_a) < 1:
            a = 0
            b = 0
        else:
            a, = tuple_a
            b = 0
    else:
        a, b = tuple_a

    if len(tuple_b) < 2:
        if len(tuple_b) < 1:
            c = 0
            d = 0
        else:
            c, = tuple_b
            d = 0
    else:
        c, d = tuple_b

    e = a + c, b + d
    return e
