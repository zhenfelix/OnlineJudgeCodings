import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
# from math import *
from itertools import *
from math import *
from string import ascii_lowercase

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

MOD = 10**9+7
def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    flag = [0]*n 
    seen = set()
    for i in range(n)[::-1]:
        if arr[i] not in seen:
            flag[i] =  1
            seen.add(arr[i])
    ans = 0
    seen = set()
    for i in range(n):
        seen.add(arr[i])
        if flag[i] == 1:
            ans += len(seen)
    print(ans)
    return 


t = int(input())
for _ in range(t):
    solve()
