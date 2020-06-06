import sys, heapq
from collections import *
from functools import lru_cache

sys.setrecursionlimit(10 ** 6)


def main():
    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split(' '))
        fmin, fmax, res = 1, a, a
        while fmin * fmin <= a:
            if a % fmin == 0:
                fmax = a//fmin
                if fmax <= b:
                    break
                if fmin <= b:
                    res = fmax
            fmin += 1
        if fmax <= b:
            print(fmin)
        else:
            print(res)


if __name__ == "__main__":
    main()




