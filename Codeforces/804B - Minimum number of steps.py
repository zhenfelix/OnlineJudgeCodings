ans = a = 0
p = int(1e9 + 7)
for c in input():
    if c == 'a':
        a = (a * 2 + 1) % p
    else:
        ans += a
print(ans % p)
 


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

MOD = 10**9+7
def solve():
    s = input().strip()
    ans = a = 0
    for ch in s:
        if ch == 'a':
            a += 1
        else:
            ans += pow(2,a,MOD)-1
            ans %= MOD 
    print(ans)
    return 


t = 1
import random
for i in range(t):
    solve()
