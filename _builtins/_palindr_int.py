"""
https://www.hackerrank.com/challenges/any-or-all/problem

You are given a space separated list of integers.
If all the integers are positive, then you need to check if any integer is a palindromic integer.
"""

def is_palindr(val):
    if 0 < val < 10:
        return True

    val = str(val)
    rank = len(val)

    for l_i, r_i in enumerate(reversed(range(rank))):
        if val[l_i] != val[r_i]:
            return False
    return True


if __name__ == "__main__":
    N = int(input().strip())
    if not (0 < N < 100):
        raise ValueError

    N_vals = list(map(int, input().strip().split()))[:N]

    res = False

    if all((x > 0 for x in N_vals)):
        if any((is_palindr(y) for y in N_vals)):
            res = True
    print(res)
