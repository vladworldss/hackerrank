# ginortS.py
"""
You are given a string .
contains alphanumeric characters only.
Your task is to sort the string in the following manner:

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234

Sample Output

ginortS132
"""

def priority(s):
    if s.islower():
        return ord(s)
    elif s.isupper():
        return ord(s)*100
    elif s in '13579':
        return ord(s) * 1000
    else:
        return ord(s) * 10000000


if __name__ == "__main__":

    inp_str = input().strip()
    if not (0 < len(inp_str) < 1000):
        raise ValueError("Bad size of str")

    print(*sorted(inp_str, key=priority), sep="")
