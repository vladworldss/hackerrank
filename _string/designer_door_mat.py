# coding: utf-8
# designer_door_mat.py
"""
Task descr: https://www.hackerrank.com/challenges/designer-door-mat/problem

Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:

    + Mat size must be X. ( is an odd natural number, and is times .)
    + The design should have 'WELCOME' written in the center.
    + The design pattern should only use |, . and - characters.
"""


def get_empty_canvas(hight, width):
    return tuple([["-" for _ in range(width)] for _ in range(hight)])


def insert_prt(li, median, count):
    right_part = median + 2 + 3*(count//2)
    left_part = median - 1 - 3 * (count // 2)
    filled = ".|."*count

    li[left_part:right_part] = filled


def insert_welcome(insert_row, median):
    insert_row[median-3:median+4] = "WELCOME"


def make_door(hight, width):

    door = get_empty_canvas(hight, width)

    h_median, w_median = hight//2, width // 2

    for row_idx in range(h_median):
        count = 1 + 2*row_idx
        insert_prt(door[row_idx], w_median, count)
        insert_prt(door[hight-row_idx-1], w_median, count)

    insert_welcome(door[h_median], w_median)
    return door


def print_door(door):
    for row in door:
        print("".join(row))


if __name__ == "__main__":
    N, M = list(map(int, input().split()))

    if N%2 == 0:
        raise ValueError("N must be odd")

    elif N<6 or N>100:
        raise ValueError("N must be in  (5, 101)")

    elif M / N != 3:
        raise ValueError("M must be equal 3 times N")

    elif M<16 or M>302:
        raise ValueError("M must be in  (15, 303)")

    door = make_door(N, M)
    print_door(door)
