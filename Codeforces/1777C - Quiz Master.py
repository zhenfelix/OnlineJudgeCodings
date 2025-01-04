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
def solve(cover):
    n, m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr = sorted(list(set(arr)))   
    n = len(arr)
    cc = Counter()
    cnt = 0 
    l = 0
    ans = inf 
    for r in range(n):
        for f in cover[arr[r]]:
            if f > m: break 
            if cc[f] == 0: cnt += 1
            cc[f] += 1
        while cnt == m:
            ans = min(ans, arr[r]-arr[l])
            for f in cover[arr[l]]:
                if f > m: break
                cc[f] -= 1
                if cc[f] == 0: cnt -= 1
            l += 1
    print(ans if ans < inf else -1)
        

mx = 10**5
cover = [set() for _ in range(mx+1)]
for i in range(1,mx+1):
    for j in range(i,mx+1,i):
        cover[j].add(i)
# t = 1
t = int(input())
import random
for i in range(t):
    solve(cover)
    # print(i)
    # if solve():
    #     print("YES")
    # else:
    #     print("NO")
