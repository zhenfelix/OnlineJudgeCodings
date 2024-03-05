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
    hq = [(-a,i) for i, a in enumerate(arr)]
    heapify(hq)
    ans = [-1]*n 
    for j in range(n)[::-1]:
        while hq and hq[0][0] < -arr[j]:
            _, i = heappop(hq)
            if i < j: ans[i] = j-i-1
    print(*ans)
    return 


t = 1
# t = int(input())
import random
for i in range(t):
    solve()
