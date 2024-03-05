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
    m = int(input())
    brr = list(map(int,input().split()))
    arr.sort()
    brr.sort()
    @lru_cache(None)
    def dfs(i,j):
        if i == n or j == m: return 0
        ans = max(dfs(i+1,j),dfs(i,j+1))
        if abs(arr[i]-brr[j]) <= 1: ans = max(ans,dfs(i+1,j+1)+1)
        return ans
    print(dfs(0,0))
    return 


t = 1
# t = int(input())
import random
for i in range(t):
    # print(i)
    solve()
