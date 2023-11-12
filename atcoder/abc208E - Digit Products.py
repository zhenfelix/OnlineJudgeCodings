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
    s, k = list(map(int,input().split()))
    arr = list(map(int,list(str(s))))
    n = len(arr)
    @lru_cache(None)
    def dfs(i,flag,zero,x):
        if i == n:
            return 1 if x <= k else 0
        hi = arr[i] if flag else 9
        ans = 0
        if zero: x = 1
        for y in range(hi+1):
            ans += dfs(i+1,flag and y == hi,zero and y == 0,x*y)
        # print(i,flag,zero,x,ans)
        return ans 

    return dfs(0,1,1,1)-1 


print(solve())
