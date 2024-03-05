import sys,os

# sys.stdin = open("input","r") 

input = sys.stdin.readline


from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
# from math import *
from itertools import *
from math import *
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

MOD = 10**9+7
def solve():
    t = int(input())
    arr = []
    for _ in range(t):
        arr.append(int(input()))
    mx = max(arr)
    ps = []
    for x in range(1,mx+1):
        s = str(x)
        i, j = 0, len(s)-1
        flag = True 
        while i < j:
            if s[i] != s[j]:
                flag = False
                break 
            i += 1
            j -= 1
        if flag:
            ps.append(x)
    m = len(ps)
    dp = [0]*(mx+1)
    dp[0] = 1
    for p in ps:
        for x in range(p,mx+1):
            dp[x] += dp[x-p]
            dp[x] %= MOD 
    for a in arr:
        print(dp[a])
    return



# t = int(input())
t = 1
for _ in range(t):
    solve()
