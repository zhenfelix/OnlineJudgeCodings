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

n = int(input())
arr = list(map(int,input().split()))
s = input()
# arr = list(map(int,input().split()))
# n = int(input())
# L, N1, N2 = list(map(int,input().split()))

def solve():
    m, x = [0]*3, [0]*3 
    ans = 0
    for i, ch in enumerate(s):
        if ch == 'X':
            x[arr[i]] += 1
    for i, ch in enumerate(s):
        if ch == 'X':
            x[arr[i]] -= 1
        elif ch == 'M':
            m[arr[i]] += 1
        else:
            e = arr[i]
            # print(m,x,e)
            for j in range(3):
                if m[j]:
                    for k in range(3):
                        if x[k]:
                            v = (1<<j)|(1<<k)|(1<<e)
                            for z in range(4):
                                if (v>>z)&1 == 0:
                                    # print(z,j,k)
                                    ans += z*m[j]*x[k]
                                    break
    return ans 

print(solve())