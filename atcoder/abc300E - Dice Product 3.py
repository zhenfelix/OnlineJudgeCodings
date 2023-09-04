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
MOD = 998244353
# base = pow(6,MOD-2,MOD)
base = pow(6,MOD-2,MOD)
base2 = pow(5,MOD-2,MOD)

@lru_cache(None)
def dfs(cur):
    if cur == 1:
        return 1 
    ans = 0
    for f in range(2,7):
        if cur%f == 0:
            # ans = (ans+base*dfs(cur//f))%MOD 
            ans = (ans+base*dfs(cur//f)*base2*6)%MOD 
    return ans 

print(dfs(n))
