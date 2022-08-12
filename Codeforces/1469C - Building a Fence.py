import sys, heapq
from collections import *
from functools import lru_cache



def main():

    def solve():
        n, k = map(int,input().split())
        arr = list(map(int, input().split()))
        lo, hi = arr[0], arr[0]
        for h in arr[1:]:
            lo = max(lo-(k-1), h)
            hi = min(hi+k-1, h+k-1)
            if lo > hi:
                print("NO")
                return
            # print(lo,hi)
        if lo <= arr[-1] <= hi:
            print("YES")
        else:
            print("NO")
        return 

    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    t = int(input())
    while t:
        t -= 1
        solve()



if __name__ == "__main__":
    main()


