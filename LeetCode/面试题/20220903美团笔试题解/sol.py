from collections import *
from functools import *
from heapq import * 
import sys 



def solve():
    n, m, k = list(map(int, input().split()))
    k -= 1
    c = list(map(int, input().split()))
    c = [i-1 for i in c]
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dp = [-float('inf')]*n
    dp[k] = 0
    mx = [k,-1]
    for i, v in enumerate(c):
        tmp = dp[v]+a[i]
        if mx[-1] == -1:
            tmp = max(tmp, (-float('inf') if mx[0] == v else dp[mx[0]])+
b[i])
        else:
            tmp = max(tmp, (dp[mx[-1]] if mx[0] == v else dp[mx[0]])+
b[i])
        dp[v] = tmp 
        if dp[v] > dp[mx[0]]:
            mx = [v,mx[0]]
        elif (mx[-1] == -1 or (mx[-1] != -1 and dp[v] > dp[mx[-1]])) and v != mx[0]:
            mx[-1] = v 
        if mx[-1] != -1 and dp[mx[0]] < dp[mx[-1]]:
            dp[0], dp[-1] = dp[-1], dp[0]
    print(max(dp))
    return  


# sys.stdin = open('duipai/data.in', 'r')
# print(solve())
solve()