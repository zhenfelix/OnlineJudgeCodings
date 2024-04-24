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
def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    cc = Counter(arr)
    mx = 0
    for i in range(n+1):
        if cc[i] == 0:
            mx = i 
            break 
    dp = [inf]*(mx+1)
    dp[0] = 0
    for i in range(1,mx+1):
        for j in range(i):
            dp[i] = min(dp[i], dp[j]+(cc[j]-1)*i+j)
    print(dp[mx])



# t = 1
t = int(input())
import random
for i in range(t):
    solve()
    # print(i)
    # if solve():
    #     print("YES")
    # else:
    #     print("NO")
