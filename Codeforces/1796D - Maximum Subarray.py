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
    n, k, x = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # if t == 10000 and idx == 36:
    #     print(n,k,x)
    #     print(*arr)
    #     return
    if x < 0:
        x = -x 
        k = n-k 
    q = deque([(-x,0,-1)])
    ans = s = 0
    mi = inf 
    pi = -1
    arr.append(0)
    for i in range(n):
        s += arr[i]
        arr[i] = s 
        while q and q[0][-1] < i-k:
            _, ps, j = q.popleft()
        while pi < i-k:
            mi = min(mi,arr[pi]-pi*x)
            ans = max(ans,2*k*x+s-i*x-mi)
            pi += 1
        if q:
            ms, ps, j = q[0]
            ans = max(ans,s+i*x-ms)
        while q and q[-1][0] >= s+i*x:
            q.pop()
        q.append((s+i*x,s,i))
    print(ans)


# t = 1
t = int(input())
import random
for i in range(t):
    solve(i)
    # print(i)
    # if solve():
    #     print("YES")
    # else:
    #     print("NO")
