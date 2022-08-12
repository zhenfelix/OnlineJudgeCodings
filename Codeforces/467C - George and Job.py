import sys, heapq
from collections import *
from functools import lru_cache



def main():

    def solve(arr,m,k):
        n = len(arr)
        presums = [0]
        for cur in arr:
            presums.append(presums[-1]+cur)
        dp = [0]*(n+1)
        for _ in range(k):
            ndp = [0]*(n+1)
            for i in range(n):
                if i >= m-1:
                    ndp[i] = max(ndp[i-1], dp[i-m]+presums[i+1]-presums[i-m+1])
            dp = ndp 
            # print(dp)
        return max(dp)

    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    n, m, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    t = 1
    for _ in range(t):
        print(solve(arr,m,k))

    # debug(ans)


if __name__ == "__main__":
    main()


