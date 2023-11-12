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
    # n, k = list(map(int, input().split()))
    s = input().strip()
    n = len(s) 

    dp = [[[0]*2 for _ in range(2)] for _ in range(n+1)]
    dp[-1][0][0] = dp[-1][0][1] = 1
    for i in range(n):
        ch = s[i]
        for cur in range(2):
            for nxt in range(2):
                ans = 0
                if ch == '*' or ch == '?':
                    if cur == 1 or ch == '?':
                        ans = dp[i-1][0][cur]+dp[i-1][1][cur]
                elif cur == 0:
                    for pre in range(2):
                        if pre+nxt == int(ch):
                            ans += dp[i-1][pre][cur]
                dp[i][cur][nxt] = ans%MOD

    print((dp[n-1][0][0]+dp[n-1][1][0])%MOD)
    return



# t = int(input())
t = 1
for _ in range(t):
    solve()
