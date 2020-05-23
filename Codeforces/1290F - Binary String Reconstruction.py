import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():

    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        # n = int(input())
        n0,n1,n2 = list(map(int, input().split(' ')))
        if n1 == 0:
            res = '0' if n0 > 0 else '1'
        elif n1 == 1:
            res = '01'
        else:
            res = '01'*((n1+1)//2)
        res = '0'*n0+res
        if n1>1 and n1%2 == 0: res = '1'+res
        res = res+'1'*n2

        print(res)




if __name__ == "__main__":
    main()


