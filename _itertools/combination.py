# coding: utf-8
from itertools import combinations


def _combinations():
    S, k = input().split()
    k = int(k)
    if not 0 < k <= len(S):
        return
    S = ''.join(sorted((x for x in S if x.isupper())))

    for i in range(1, k+1):
        pers = sorted(list(combinations(S, i)))
        for x in pers:
            print(''.join(x))

_combinations()