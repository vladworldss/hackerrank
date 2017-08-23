# coding: utf-8


def minion_game(s):
    r = [0, 0]
    for i, c in enumerate(s):
        r[c in 'AEIOU'] += len(s) - i

    res = 'Draw'
    if r[0] > r[1]:
        res = 'Stuart {0}'.format(r[0])
    elif r[0] < r[1]:
        res = 'Kevin {0}'.format(r[1])
    print(res)
    return res

def minion_game_test():
    minion_game('BANANA') == 'Stuart 12'


def merge_the_tools(string, k):
    l = len(string) // k
    for i in range(l):
        t = ''
        for c in string[i * k:i * k + k]:
            if c not in t: t += c
        print(t)

merge_the_tools('AABCASDSDAADA', 5)