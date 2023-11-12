import sys,os
input = sys.stdin.readline
# sys.stdin = open("input","r") 

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
    n, k, q = list(map(int, input().split()))
    mx = 2*10**5+10
    arr = [0]*mx 
    for _ in range(n):
        a, b = list(map(int, input().split()))
        arr[a] += 1
        arr[b+1] -= 1
    for a in range(1,mx):
        arr[a] += arr[a-1]
    cnt = [0]*mx 
    for a in range(1,mx):
        if arr[a] >= k:
            cnt[a] = 1
        cnt[a] += cnt[a-1]
    for _ in range(q):
        a, b = list(map(int, input().split()))
        print(cnt[b]-cnt[a-1])


# t = int(input())
t = 1
for _ in range(t):
    solve()
