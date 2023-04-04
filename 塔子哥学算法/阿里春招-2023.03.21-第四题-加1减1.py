    from random import *
    import sys
    from collections import * 
    from math import * 

    def solve():
        # sys.stdin = open('contests/input', 'r')
        n, k = list(map(int,input().split()))
        arr = list(map(int,input().split()))
        def check(t):
            res = inf
            cur = 0 
            for i in range(n):
                cur += abs(arr[i]-t)
                if i >= k: cur -= abs(arr[i-k]-t)
                if i >= k-1: res = min(res, cur)
            return res 
        return min(check(i) for i in range(10))

    print(solve())