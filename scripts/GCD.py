# -*- coding: utf-8 -*-
"""
Generates greatest common factor of 2 numbers using Euclidean Algorithm.

Requirements:
    -> Python 3.0 or higher

"""
__script_name__ = "Greatest Common Divisor (Euclidean Algorithm)"
__version__ = "0.1.0"
__author__ = "Mayank Thakur"
__date__ = "27-02-2020"


def gcd(a, b):
    if 0 in [a,b]:
        return max([a,b])

    if a>b:
        a = a-b
        return gcd(a, b)
    else:
        b = b-a
        return gcd(a, b)


if __name__ == '__main__':
    print(gcd(270, 192))

    # to run gcd for an array
    arr = [2, 4, 3, 6]
    gcd_result = [0]
    gcd_result = [gcd(gcd_result[-1], x) for x in arr]
    print(gcd_result)
