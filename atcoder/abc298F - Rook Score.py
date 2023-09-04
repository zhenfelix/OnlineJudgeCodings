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
mp = dict()
xs = defaultdict(int)
ys = defaultdict(int)
for _ in range(n):
    x, y, v = list(map(int,input().split()))
    mp[x,y] = v 
    xs[x] += v 
    ys[y] += v 
xarr = [[x,v] for x, v in xs.items()]
yarr = [[y,v] for y, v in ys.items()]
xarr.sort(key=lambda a: -a[-1])
yarr.sort(key=lambda a: -a[-1])
ans = 0
for (x,y), v in mp.items():
    ans = max(ans, xs[x]+ys[y]-mp[x,y])
for x, vx in xarr:
    for y, vy in yarr:
        if (x,y) not in mp:
            ans = max(ans, vx+vy)
            break 
print(ans)
