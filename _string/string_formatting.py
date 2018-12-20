# coding: utf-8
"""
source: https://www.hackerrank.com/challenges/python-string-formatting/problem

Given an integer, , print the following values for each integer from 1 to n:
    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary

The four values must be printed on a single line in the order specified above for each i
from 1 to n. Each value should be space-padded to match the width of the binary value of n.

Input Format
A single integer denoting n.

Constraints
1<=n<=99

Output Format
Print n lines where each line (in the range 1<=i<=n) contains the respective decimal,
octal, capitalized hexadecimal, and binary values of i.
Each printed value must be formatted to the width of the binary value of n.
"""


def print_formatted(number):
    width = len('{:b}'.format(number))

    for i in range(1, number + 1):
        print(str.rjust(str(i), width), \
        str.rjust('{:o}'.format(i), width), \
        str.rjust('{:X}'.format(i), width), \
        str.rjust('{:b}'.format(i), width))


if __name__ == '__main__':
    N = int(input())
