import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)
import operator as op
from functools import reduce



def main():

    def ncr(n, r):
        r = min(r, n - r)
        numer = reduce(op.mul, range(n, n - r, -1), 1)
        denom = reduce(op.mul, range(1, r + 1), 1)
        return numer // denom

    # sys.stdin = open('input.txt', 'r')


    t = int(input())

    for _ in range(t):
        x1,y1,x2,y2 = map(int,input().split(' '))
        x, y = x2-x1, y2-y1
        print(x*y+1)









if __name__ == "__main__":
    main()
