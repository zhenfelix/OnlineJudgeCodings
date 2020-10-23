import sys
from collections import Counter
from functools import lru_cache
# sys.stdin = open("input.txt", "r")


# def solve(arr):
#     presum = [0]+arr 
#     for i, x in enumerate(presum):
#         if i > 0:
#             presum[i] += presum[i-1]
#     @lru_cache(None)
#     def dfs(i,j):
#         if i == j:
#             return 0
#         res = 0
#         for k in range(i,j):
#             # res += (sum(arr[i:j+1])+dfs(i,k)+dfs(k+1,j))/(j-i)
#             res += (presum[j+1]-presum[i]+dfs(i, k)+dfs(k+1, j))/(j-i)
#         return res
#     return dfs(0,len(arr)-1)

# def solve(arr):
#     n = len(arr)
#     res = 0
#     for mid in range(n-1):
#         for i in range(mid+1):
#             res += arr[i]/(mid-i+1)
#         for i in range(mid+1,n):
#             res += arr[i]/(i-mid)
#     return res 

def solve(arr):
    n = len(arr)
    res, prob = 0, sum(1/i for i in range(1,n))

    for i in range(n):
        res += arr[i]*prob 
        if i < n-1:
            prob -= 1/(n-1-i)
            prob += 1/(i+1)
    return res


t = int(input())
for i in range(t):
    t = int(input())
    arr = list(map(int, input().split()))
    res = solve(arr)
    print("Case #{}: {}".format(i+1, res))
