import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
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

n, m = list(map(int,input().split()))
arr = list(map(int,input().split()))
# arr = list(map(int,input().split()))
# n = int(input())
# L, N1, N2 = list(map(int,input().split()))

def solve():
    mp = defaultdict(list)
    for i, v in enumerate(arr):
        mp[v].append(i)
    for v in range(n+1):
        if not mp[v]: return v 
        pre = -1
        for i in mp[v]:
            if i-pre-1 >= m: return v 
            pre = i 
        if n-pre-1 >= m: return v 
    return -1 

print(solve())


n, m = list(map(int,input().split()))
nums = list(map(int,input().split()))
pos = [0] * n
seps = [-1] * (n + 1)

for i, v in enumerate(nums):
    seps[v] = max(seps[v], i - pos[v])
    pos[v] = i + 1

for i in range(n):
    seps[i] = max(seps[i], n - pos[i])

for i in range(n + 1):
    if seps[i] >= m or seps[i] == -1:
        print(i)
        break
