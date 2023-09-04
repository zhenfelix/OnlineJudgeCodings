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

# n, s = list(map(int,input().split()))
# arr = list(map(int,input().split()))
# n = int(input())
L, N1, N2 = list(map(int,input().split()))

arr, brr = [], []
for _ in range(N1):
    v, c = list(map(int,input().split()))
    arr.append((v,c))
for _ in range(N2):
    v, c = list(map(int,input().split()))
    brr.append((v,c))
i, j = 0, 0
ans, cur, s1, s2 = 0, 0, 0, 0
while i < N1 and j < N2:
    pre = cur 
    v1, c1 = arr[i]
    v2, c2 = brr[j]
    flag = (v1 == v2)
    if s1+c1 < s2+c2:
        s1 += c1 
        cur = s1
        i += 1
    elif s1+c1 > s2+c2:
        s2 += c2 
        cur = s2 
        j += 1
    else:
        s1 += c1 
        s2 += c2 
        cur = s1 
        i += 1
        j += 1 
    if flag:
        ans += cur-pre 
print(ans)