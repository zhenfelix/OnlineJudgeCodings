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
    arr = []
    for _ in range(n):
        l, r = list(map(int,input().split()))
        arr.append((l,r))
    e1, e2 = -1, -1
    for l, r in sorted(arr):
        if l > e1:
            e1 = r 
        elif l > e2:
            e2 = r 
        else:
            return False
    return True
    


t = 1
# t = int(input())
import random
for i in range(t):
    # solve()
    # print(i)
    if solve():
        print("YES")
    else:
        print("NO")
