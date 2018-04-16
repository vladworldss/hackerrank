# coding: utf-8
"""
https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""


def solve(a0, a1, a2, b0, b1, b2):
    pairs = zip([a0, a1, a2], [b0, b1, b2])
    alice = bob = 0
    for a, b in pairs:
        if a > b:
            alice += 1
        elif a < b:
            bob += 1
    return alice, bob


def test():
    assert solve(5, 6, 7, 3, 6, 10) == [1, 1]


if __name__ == '__main__':

    a0, a1, a2 = list(map(int, input().strip().split(' ')))
    b0, b1, b2 = list(map(int, input().strip().split(' ')))

    result = solve(a0, a1, a2, b0, b1, b2)
    print (" ".join(map(str, result)))
