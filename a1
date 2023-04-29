"""
Hannah Lee
Section: AE

This file has three methods that are being tested in the file
a1_test.py.
"""


def funky_sum(a: float, b: float, mix: float) -> float:
    """
    Returns funky sum of given a and b depending on the given mix.
    If mix is 0 or less, the result should be the same as a. If
    mix is 1 or more, the result should be the same as b. For any
    value of mix between 0 and 1, it should add 1 - mix times a and
    mix times b.
    """
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    return ((1 - mix) * a) + (mix * b)


def total(n: int) -> int | None:
    """
    Returns sum of integers within range 0 - given n (inclusive)
    If n is negative, the function should return the value None instead
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def swip_swap(source: str, c1: str, c2: str) -> str:
    """
    Swaps the two given characters in the given source string and returns
    a string of the word with the swapped characters. Can assume that c1 and
    c2 are single characters.
    """
    switched = ""
    for char in source:
        if char == c1:
            switched += c2
        elif char == c2:
            switched += c1
        else:
            switched += char
    return switched
