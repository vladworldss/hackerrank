'''
https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

Task

 is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi
amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.
'''


'''
Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''

'''
Sample Output

200

'''

from collections import Counter


if __name__ == '__main__':
    X = int(input())
    N = map(int, input().split())
    x = int(input())
    L = map(tuple, (map(int, input().split()) for _ in range(x)))
    n = Counter(N)
    p = 0
    for shoe_size, price in L:
        if shoe_size in n and n[shoe_size] > 0:
            n[shoe_size] -= 1
            p += price

    print(p)
