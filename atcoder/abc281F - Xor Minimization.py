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
N = 33*n 
child = [[-1,-1] for _ in range(N)]
limit = 1
for a in arr:
    cur = 0
    for i in range(32)[::-1]:
        idx = (a>>i)&1
        pre = cur 
        cur = child[cur][idx]
        if cur == -1:
            cur = limit
            limit += 1
            child[pre][idx] = cur 
# print(child)
@bootstrap
def dfs(cur,i):
    if child[cur][0] > 0 and child[cur][1] > 0:
        a = yield dfs(child[cur][0],i-1)
        b = yield dfs(child[cur][1],i-1)
        yield (1<<i)|min(a,b)
    if child[cur][0] > 0:
        a = yield dfs(child[cur][0],i-1)
        yield a 
    if child[cur][1] > 0:
        b = yield dfs(child[cur][1],i-1)
        yield b
    yield 0

print(dfs(0,31))
