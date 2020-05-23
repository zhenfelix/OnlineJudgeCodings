import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**8)



def main():

    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        s = set([0])
        n = int(input())
        arr = list(map(int, input().split(' ')))
        arr.sort()
        for a in arr:
            if a in s:
                n -= 1
            for c in range(a,arr[-1]+1):
                if c-a in s: s.add(c)
        print(n)


if __name__ == "__main__":
    main()


