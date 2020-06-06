import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():




    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        n, m = map(int,input().split(' '))
        total = n*m
        print(total//2+(total&1))





if __name__ == "__main__":
    main()



 