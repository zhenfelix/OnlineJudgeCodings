import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():

    def solve(n,k):
        if k%10 == 0:
            return 1 if k <= n else 0
        s = str(k)
        k2 = int(s[::-1])
        if k2 < k:
            return 0
        def calc(x):
            cnt = 0
            while x <= n:
                cnt += 1
                x *= 10
            return cnt
        if k == k2:
            return calc(k)
        return calc(k)+calc(k2)



    # sys.stdin = open('input.txt', 'r')
    # print(input().split(' '))
    n, k = map(int, input().split(' '))
    ans = solve(n,k)
    print(ans)


if __name__ == "__main__":
    main()


