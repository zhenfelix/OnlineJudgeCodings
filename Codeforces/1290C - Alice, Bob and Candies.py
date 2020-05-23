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
        a, b, cur, i, j, flag, cnt = 0, 0, 0, 0, n-1, -1, 0
        while i <= j:
            delta = 0
            if flag == -1:
                while i<=j and delta <= cur:
                    delta += arr[i]
                    i += 1
                a += delta
            else:
                while i<= j and delta <= cur:
                    delta += arr[j]
                    j -= 1
                b += delta
            flag *= -1
            cur = delta
            cnt += 1
        print(cnt,a,b)


if __name__ == "__main__":
    main()


