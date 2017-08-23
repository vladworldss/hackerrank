# coding: utf-8

def wrap(string, max_width):
    import textwrap

    string = string[:1000]
    if max_width > len(string):
        raise Exception()

    w = textwrap.fill(string, max_width)
    print(w)

wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)