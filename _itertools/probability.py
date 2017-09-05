from itertools import combinations

def _prob():
    size = int(input().strip())
    s = input().strip().split()
    s = s[:size]
    k = int(input().strip())

    comb = tuple(combinations(range(1, len(s)+1), k))
    comb_size = len(comb)

    a_idx = set()
    for i, ch in enumerate(s, 1):
        if ch == 'a':
            a_idx.add(i)
    a_count = 0
    for pair in comb:
        if any(x in pair for x in a_idx):
            a_count += 1
    res = a_count/comb_size
    print('%0.3f'%res)

_prob()

"""
4
a a c d
2
0.833
"""