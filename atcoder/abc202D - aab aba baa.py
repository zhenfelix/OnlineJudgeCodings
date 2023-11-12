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
    import math 
    a, b, k = list(map(int,input().split()))
    ans = []
    while a or b:
        if k > math.comb(a+b-1,b):
            k -= math.comb(a+b-1,b)
            ans.append('b')
            b -= 1
        else:
            ans.append('a')
            a -= 1    
    return ''.join(ans) 
    

print(solve())
