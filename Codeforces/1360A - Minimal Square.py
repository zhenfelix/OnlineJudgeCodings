import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():


    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split(' '))
        if a > b:
            a, b = b, a
        d = max(b,2*a)
        d *= d
        print(d)



if __name__ == "__main__":
    main()




