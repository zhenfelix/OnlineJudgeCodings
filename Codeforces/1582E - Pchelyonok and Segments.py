import sys, heapq
from collections import *
from functools import lru_cache



def main():

    def solve(arr):
        n = len(arr)
        arr = arr[::-1]
        # print(arr)
        presums = [0]
        for cur in arr:
            presums.append(presums[-1]+cur)
        dp = [float('inf')]*(n+1)
        k = 1
        while True:
            ndp = [0]*(n+1)
            for i in range(n):
                ndp[i] = ndp[i-1]
                if i >= k-1 and presums[i+1]-presums[i-k+1] < dp[i-k]:
                    ndp[i] = max(ndp[i], presums[i+1]-presums[i-k+1])
            dp = ndp 
            # print(dp)
            if dp[n-1] == 0:
                break
            k += 1
            
        return k-1

    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))

    # debug(ans)


if __name__ == "__main__":
    main()


