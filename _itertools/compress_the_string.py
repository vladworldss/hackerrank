from itertools import groupby


def _group(s=None):
    if s is None:
        s = input().strip()
    res = ' '.join('({}, {})'.format(len(tuple(x[1])), x[0]) for x in groupby(s))
    return res


def test_group():
    assert _group('1222311') == '(1, 1) (3, 2) (1, 3) (2, 1)'

res = _group()
print(res)