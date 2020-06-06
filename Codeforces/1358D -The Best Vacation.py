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

    n, x = map(int, input().split(' '))
    arr = list(map(int,input().split(' ')))
    arr += arr.copy()
    days, hugs = [0]+arr.copy(), [0]+list(map(lambda x: x*(x+1)//2,arr))
    for i in range(1,2*n+1):
        days[i] += days[i-1]
        hugs[i] += hugs[i-1]
    res = 0
    for i in range(1,2*n+1):
        y = days[i]-x
        j = bisect.bisect_right(days,y,0,i)
        y -= days[j-1]
        res = max(res, hugs[i]-hugs[j-1]-y*(y+1)//2)
    print(res)


if __name__ == "__main__":
    main()
