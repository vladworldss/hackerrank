# coding: utf-8


def swap_case(s):
    def foo(ch):
        res = ''
        if ch.isupper():
            res = ch.lower()
        else:
            res = ch.upper()
        return res

    if not isinstance(s, str):
        raise TypeError()
    return ''.join(map(foo, s[:1000]))


def swap_case_test():
    assert swap_case('HackerRank.com presents "Pythonist 2".') == 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'


def string_split_and_join(line):
    if not isinstance(line, str):
        raise TypeError()
    return line.replace(' ', '-')

def print_full_name(a, b):
    a, b = a.strip(), b.strip()
    msg = "Hello {} {}! You just delved into python.".format(a, b)
    print(msg)


def count_substring(string, sub_string):
    from _string import ascii_letters

    rule = ascii_letters + ''.join((str(x) for x in range(10)))
    string = string[:200]
    subs_size = len(sub_string)
    res = 0

    for i, ch in enumerate(string):
        if (ch in rule) and (ch == sub_string[0]):
            compare = string[i:i+subs_size]
            if compare == sub_string:
                res += 1
                continue
    return res


def count_substring_test():
    assert count_substring('12jlka445kljakldfjlaksjdfdka3942', '3942') == 1
    assert count_substring('ABCBCCBC', 'CBC') == 2


def string_validators(line=None):
    from _string import ascii_letters

    if line is None:
        line = input().strip()[:1000]

    digits = ''.join((str(x) for x in range(10)))
    alnum = ascii_letters + digits
    lowers = set(ascii_letters.lower())
    uppers = set(ascii_letters.upper())
    rules = {
        0: alnum,
        1: ascii_letters,
        2: digits,
        3: lowers,
        4: uppers
    }
    results = []

    for i in range(5):
        res = False

        rule = rules[i]
        if any(ch in rule for ch in line):
            res = True
        print(res)
        results.append(res)


def string_validators_test():
    assert string_validators('qRA2') == list((True for _ in range(5)))
