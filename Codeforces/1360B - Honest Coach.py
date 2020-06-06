import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():


    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split(' ')))
        arr.sort()
        res = float('inf')
        for i in range(1,n):
            res = min(res,arr[i]-arr[i-1])
            if res == 0:
                break
        print(res)



if __name__ == "__main__":
    main()




