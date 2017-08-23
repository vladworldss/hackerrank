# coding: utf-8
from itertools import permutations


def _permutations():
    S, k = input().split()
    k = int(k)
    if not 0 < k <= len(S):
        return
    S = ''.join((x for x in S if x.isupper()))
    pers = sorted(list(permutations(S, k)))
    for x in pers:
        print(''.join(x))
