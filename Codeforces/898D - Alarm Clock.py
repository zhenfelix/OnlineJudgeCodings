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
    n, m, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr.sort()
    # if t == 10000 and idx == 36:
    #     print(n,k,x)
    #     print(*arr)
    #     return
    ans = cnt = l = 0
    visited = [0]*n 
    for r in range(n):
        cnt += 1
        visited[r] = 1
        while arr[r]-arr[l] >= m:
            cnt -= visited[l]
            l += 1
        if cnt >= k:
            visited[r] = 0
            cnt -= 1
            ans += 1
    print(ans)
            




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
