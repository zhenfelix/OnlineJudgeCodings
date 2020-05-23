import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**8)



def main():

    # sys.stdin = open('input.txt', 'r')
    n = int(input())
    arr = list(map(int,input().split(' ')))
    res = arr[0]
    for i in range(1,n):
        res += max(arr[i]-arr[i-1],0)
    print(res)



if __name__ == "__main__":
    main()


