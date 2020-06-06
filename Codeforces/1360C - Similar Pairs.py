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
        evens, odds = [], []
        for a in arr:
            if a&1: odds.append(a)
            else: evens.append(a)
        flag = False
        if len(odds)&1 == 0: flag = True
        else:
            ss = set(odds)
            for a in evens:
                if a-1 in ss or a+1 in ss:
                    flag = True
                    break
        if flag:
            print('YES')
        else:
            print('NO')



if __name__ == "__main__":
    main()




