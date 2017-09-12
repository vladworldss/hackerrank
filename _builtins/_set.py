# coding: utf-8


def average(array):
    array = set(array)
    if 0<n<=100:
        avg = sum(set(array))/len(array)
        return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
