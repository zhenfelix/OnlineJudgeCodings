import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
# from math import *
from itertools import *

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

# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int,input().split())))
# arr = list(map(int,input().split()))
# crr = list(map(int,input().split()))

# n = int(input())
# L, N1, N2 = list(map(int,input().split()))
MOD = 10**9+7
def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    pos = [[-1]*2 for _ in range(20)]
    ans = 0
    for i, v in enumerate(arr):
        p = -1
        for j in range(20):
            if v&1: pos[j].append(i)
            v >>= 1
            p = max(p,pos[j][-2])
        ans += i-p 
    return ans 


print(solve())
