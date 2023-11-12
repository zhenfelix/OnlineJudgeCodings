import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
from math import *

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

n = int(input())
# n, m = list(map(int,input().split()))
# arr = []
# for _ in range(n):
#     arr.append(list(map(int,input().split())))
arr = list(map(int,input().split()))
# n = int(input())
# L, N1, N2 = list(map(int,input().split()))

def solve():
    cur = mx = mi = 0
    ansmx = 0 
    ansmi = 0 
    for a in arr:
        if a == 0:
            a = -1
        cur += a 
        ansmx = max(ansmx, cur-mi)
        ansmi = min(ansmi, cur-mx)
        mi = min(mi, cur)
        mx = max(mx, cur)
    return ansmx-ansmi+1

print(solve())