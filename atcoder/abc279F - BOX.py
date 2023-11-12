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
    n, q = list(map(int,input().split()))
    parent = list(range(n+q))
    pseudo = list(range(n+q))
    origin = list(range(n+q))
    @bootstrap
    def find(cur):
        if parent[cur] != cur:
            parent[cur] = yield find(parent[cur])
        yield parent[cur]
    pos = n+q-1 
    k = n 
    for _ in range(q):
        ops = list(map(int,input().split()))
        if len(ops) == 3:
            x, y = ops[1:]
            x -= 1
            y -= 1
            if origin[pseudo[y]] != y:
                continue
            parent[pseudo[y]] = pseudo[x]
            pseudo[y] = pos 
            origin[pos] = y 
            pos -= 1
        elif ops[0] == 2:
            x = ops[1]
            x -= 1
            parent[k] = pseudo[x]
            k += 1
        else:
            x = ops[1]
            x -= 1
            print(origin[find(x)]+1)

    return 


solve()
