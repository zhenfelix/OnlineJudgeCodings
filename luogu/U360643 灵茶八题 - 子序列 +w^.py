https://www.luogu.com.cn/blog/endlesscheng/post-ling-cha-ba-ti-ti-mu-lie-biao

import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
from math import *

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

n = int(input())
# n, m = list(map(int,input().split()))
# arr = []
# for _ in range(n):
#     arr.append(list(map(int,input().split())))
arr = list(map(int,input().split()))
# crr = list(map(int,input().split()))

# n = int(input())
# L, N1, N2 = list(map(int,input().split()))
MOD = 10**9+7
def solve():
    ans = 0
    tot = sum(arr)
    dp = [0]*(tot+1)
    dp[0] = 1
    for a in arr:
        for s in range(a,tot+1)[::-1]:
            dp[s] ^= dp[s-a]
    for s, p in enumerate(dp):
        if p: ans ^= s
    return ans 

print(solve())