import re


def  is_digit(var):
    res = False
    pattern = re.compile('\A[+-]?[\d]+.?\d+\Z')
    if pattern.match(var):
        res = True
    return res


def test_is_digit():
    t_input = ['4.0O0', '-1.00', '+4.54', 'SomeRandomStuff']
    t_output = [False, True, True, False]
    assert [is_digit(x) for x in t_input] == t_output

test_is_digit()

if __name__ == '__main__':
    vars = [input().strip() for _ in range(int(input()))]
    for v in vars:
       print(is_digit(v))
