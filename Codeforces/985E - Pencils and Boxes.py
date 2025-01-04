import sys,os

# sys.stdin = open("input","r") 

input = sys.stdin.readline


from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
# from math import *
from itertools import *
# from math import *
from string import ascii_lowercase

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

from math import *
MOD = 10**9+7
def solve(idx):
    n,k,d = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    # print(arr)
    dp = [0]*(n+2) 
    dp[-1] = 1
    j = 0
    for i in range(n):
        while arr[i]-arr[j] > d: j += 1
        if i-j+1 >= k and dp[i-k]-dp[j-2] > 0:
            dp[i] += 1
        dp[i] += dp[i-1]
    if dp[n-1]-dp[n-2] > 0:
        print("YES")
    else:
        print("NO")
    # print(dp)
    return




t = 1
# t = int(input())
import random
for i in range(t):
    solve(i)
    # print(i)
    # if solve():
    #     print("YES")
    # else:
    #     print("NO")
