import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():
    def func(target):
        left = 1
        right = 0
        sums = 0
        while sums != target:
            if sums < target:
                right += 1
                sums += right
            else:
                sums -= left
                left += 1
        return right-left+1




    # sys.stdin = open('input.txt', 'r')
    n, m = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    for _ in range(m):
        op, lo, hi = map(int, input().split(' '))
        if op == 1:
            for i in range(lo-1,hi):
                arr[i] = func(arr[i])
        else:
            res = 0
            for i in range(lo-1,hi):
                res += arr[i]
            print(res)





if __name__ == "__main__":
    main()


