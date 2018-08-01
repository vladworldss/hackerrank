"""
There is an array of integers.
There are also disjoint sets, and , each containing integers.
You like all the integers in set and dislike all the integers in set .
Your initial happiness is .
For each integer in the array, if , you add to your happiness.
If , you add to your happiness.
Otherwise, your happiness does not change.
Output your final happiness at the end.

Note: Since and are sets, they have no repeated elements. However, the array might contain duplicate elements.
"""
from collections import defaultdict

if __name__ == "__main__":

    def to_int(ar):
        for x in ar:
            x = int(x)
            if 1<=x<=10**9:
                yield x

    n, m = list(map(int, input().strip().split()))
    if not (1 <= n <= 10**5):
        raise ValueError
    if not (1 <= m <= 10**5):
        raise ValueError

    hapiness = 0

    main_arr = list(to_int(input().strip().split()))[:n]
    main_dict = defaultdict(int)
    for x in main_arr:
        main_dict[x] += 1

    a_set = set(list(to_int(input().strip().split()))[:m])

    b_set = set(list(to_int(input().strip().split()))[:m])

    for x in a_set:
        if x in main_dict:
            hapiness += main_dict[x]

    for x in b_set:
        if x in main_dict:
            hapiness -= main_dict[x]
    print(hapiness)
