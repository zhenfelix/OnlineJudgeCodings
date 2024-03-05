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

MOD = 10**9+7
def solve():
    n, s = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    tot = sum(arr)
    ans = [0]*n 
    # left, right = arr+[0], arr+[0]
    # for i in range(n):
    #     left[i] += left[i-1]
    # for i in range(n)[::-1]:
    #     right[i] += right[i+1]
    for i in range(n):
        lo, hi = n-1, tot-arr[i]
        lo, hi = s-hi, s-lo 
        if lo > 1:
            ans[i] += min(lo-1,arr[i])
        if hi < arr[i]:
            ans[i] += min(arr[i]-hi,arr[i])
    print(*ans)

    return 


t = 1
# t = int(input())
import random
for i in range(t):
    solve()
