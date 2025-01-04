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
    n,q = list(map(int, input().split()))
    mark = [[0]*n for _ in range(2)]
    cnt = 0
    for _ in range(q):
        r,c = list(map(int, input().split()))
        r -= 1
        c -= 1
        mark[r][c] ^= 1
        delta = mark[r^1][c]
        if c > 0: delta += mark[r^1][c-1]
        if c < n-1: delta += mark[r^1][c+1]
        if mark[r][c]: cnt += delta
        else: cnt -= delta
        if cnt == 0:
            print("Yes")
        else:
            print("No")
    return




t = 1
# t = int(input())
import random
for i in range(t):
    solve(i)
    # print(i)
    # if solve():
    #     print("YES")
    # else:
    #     print("NO")
