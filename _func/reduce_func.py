"""
https://www.hackerrank.com/challenges/reduce-function/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Given a list of rational numbers,find their product.
"""


from fractions import Fraction
from functools import reduce


def product(fracs):

    numer_f = reduce(lambda x, y: x*y, (x.numerator for x in fracs))
    denom_f = reduce(lambda x, y: x*y, (x.denominator for x in fracs))

    return Fraction(numer_f, denom_f)


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
