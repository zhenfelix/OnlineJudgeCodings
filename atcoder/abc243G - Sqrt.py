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
# arr = list(map(int,input().split()))
# n = int(input())
# L, N1, N2 = list(map(int,input().split()))

def solve():
    x = int(input())
    y = int(sqrt(x))
    if y*y > x: y -= 1
    ans = 0
    for i in range(1,y+1):
        if i*i > y: break 
        ans += f[i]*(y-i*i+1)
    return ans 


N = 10**5
f = [1]*N 
j = 2
for i in range(2,N):
    f[i] = f[i-1]
    if j*j == i:
        f[i] += f[j]
        j += 1


for _ in range(n):
    print(solve())