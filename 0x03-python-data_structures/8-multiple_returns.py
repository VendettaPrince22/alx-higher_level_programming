#!/usr/bin/python3


def multiple_returns(sentence):
    """Finds the length of a string
        and its first character
    Args:
        sentence: sentence to work with
    Returns a tuple.
    """
    str_len = len(sentence)

    if str_len == 0:
        return (str_len, None)

    str_first = sentence[0]

    return (str_len, str_first)
