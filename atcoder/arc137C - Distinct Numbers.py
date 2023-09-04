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
n = int(input())
arr = list(map(int,input().split()))

flag = False
if arr[-1]-arr[-2] > 1:
    flag = True 
if not flag:
    arr.append(-1)
    delta = sum(arr[i]-arr[i-1]-1 for i in range(n))
    if delta%2 == 1:
        flag = True 
if flag:
    print("Alice")
else:
    print("Bob")
