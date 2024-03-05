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
    arr, brr = [], []
    for _ in range(n):
        tmp = list(map(int,input().split()))
        arr.append(tmp[0])
        brr.append(tmp[1])
    lo, hi = 0, n 
    while lo <= hi:
        m = (lo+hi)//2
        cnt = 0
        for i in range(n):
            if cnt <= brr[i] and m-1-cnt <= arr[i]:
                cnt += 1
        # print(cnt,m)
        if cnt >= m:
            lo = m+1
        else:
            hi = m-1
    print(hi)
    return 


# t = 1
t = int(input())
import random
for i in range(t):
    # print(i)
    solve()
