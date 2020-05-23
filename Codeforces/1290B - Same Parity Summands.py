import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():

    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split(' '))
        # n = int(input())
        nn, kk = n&1, k&1
        flag, res = False, []
        if nn ^ kk == 0:
            if n >= k:
                flag = True
                res = [n-k+1]+[1]*(k-1)
        elif nn == 0 and kk == 1:
            if n >= k*2:
                flag = True
                res = [n-k*2+2]+[2]*(k-1)
        if len(res) > 0:
            print("YES")
            print(' '.join(map(str,res)))
        else:
            print("NO")


if __name__ == "__main__":
    main()


