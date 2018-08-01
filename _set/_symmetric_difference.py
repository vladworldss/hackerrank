"""
https://www.hackerrank.com/challenges/symmetric-difference/problem

Task: Given sets of integers, and , print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either or but do not exist in both.
"""


def sym_diff(first, second):
    m_set, n_set = set(first), set(second)
    return sorted([*m_set.difference(n_set), *n_set.difference(m_set)])


def test():
    n = [8, -10]
    m = [5,6,7]
    assert list(sym_diff(n, m)) == [-10, 5, 6, 7, 8]


if __name__ == "__main__":
    M = N = 0
    m_vals = None
    n_vlas = None

    M = int(input().strip())
    m_vals = list(map(int, input().strip().split()))
    m_vals = m_vals[:M]

    N = int(input().strip())
    n_vals = list(map(int, input().strip().split()))
    n_vals = n_vals[:N]

    for x in sym_diff(m_vals, n_vals):
        print(x)
