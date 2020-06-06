import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)
import operator as op
from functools import reduce
import bisect



def main():

    # sys.stdin = open('input.txt', 'r')
    # t = int(input())
    #
    # for _ in range(t):
    #     x1,y1,x2,y2 = map(int,input().split(' '))
    #     x, y = x2-x1, y2-y1
    #     print(x*y+1)
    n = int(input())
    arr = list(map(int,input().split(' ')))
    x = int(input())

    first, cur, res = sum(arr)+x*(n-len(arr)), 0, 0
    if first > 0:
        print(n)
        return
    for k in range(len(arr),n)[::-1]:
        cur += x-arr[n-k-1]
        res = min(res,cur)
        first -= x
        if first+res > 0:
            print(k)
            return
    print(-1)
    return

if __name__ == "__main__":
    main()
