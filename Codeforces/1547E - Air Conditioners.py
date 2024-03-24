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
    _ = input()
    m, n = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    trr = list(map(int,input().split()))
    ans = [inf]*m 
    right = [(trr[i]+arr[i]-1,arr[i]-1) for i in range(n)]
    heapify(right)
    candidates = [(arr[i]-1,trr[i]-arr[i]+1) for i in range(n)]
    candidates.sort(reverse=True)
    cur = inf 
    for p in range(m):
        while candidates and candidates[-1][0] <= p:
            a, b = candidates.pop()
            cur = min(cur,b)
        ans[p] = min(ans[p], cur+p)
        while right and right[0][-1] < p:
            heappop(right)
        if right:
            ans[p] = min(ans[p],right[0][0]-p)
    print(*ans)


    


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
