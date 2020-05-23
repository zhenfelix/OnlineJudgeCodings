import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():

    def f(x):
        y = str(x)
        lo, hi = int(min(y)), int(max(y))
        return lo*hi

    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        a, k = map(int, input().split(' '))
        for _ in range(k-1):
            b = f(a)
            if b == 0: break
            a += b
        print(a)


if __name__ == "__main__":
    main()


