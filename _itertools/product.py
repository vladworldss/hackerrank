# coding: utf-8
from itertools import product


def _product():
    foo = lambda: tuple(set(map(int, input().split()[:30])))
    A = foo()
    B = foo()
    print(*product(A, B))
