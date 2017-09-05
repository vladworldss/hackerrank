from operator import itemgetter
from itertools import groupby

def person_lister(f):
    def inner(people):
        res = []
        for i, x in enumerate(people):
        	x[2] = int(x[2]) 
        people.sort(key=itemgetter(2))
        y = groupby(people, itemgetter(2))
        for elt, items in y:
        	for x in items:
        		res.append(f(x))
        return res
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# INPUT
"""
10
Jake Jake 42 M
Jake Kevin 57 M
Jake Michael 91 M
Kevin Jake 2 M
Kevin Kevin 44 M
Kevin Michael 100 M
Michael Jake 4 M
Michael Kevin 36 M
Michael Michael 15 M
Micheal Micheal 6 M
"""
# OUTPUT
"""
Mr. Kevin Jake
Mr. Michael Jake
Mr. Micheal Micheal
Mr. Michael Michael
Mr. Michael Kevin
Mr. Jake Jake
Mr. Kevin Kevin
Mr. Jake Kevin
Mr. Jake Michael
Mr. Kevin Michael
"""