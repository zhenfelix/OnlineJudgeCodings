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

from math import *
MOD = 10**9+7
def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    g = defaultdict(list)
    for i in range(1,n):
        p = arr[i-1]
        g[p-1].append(i)
    cnt = [1]*n 
    @bootstrap
    def dfs(cur):
        for nxt in g[cur]:
            yield dfs(nxt)
            cnt[cur] += cnt[nxt]
        yield
    dfs(0)
    ans = [0]*n 
    @bootstrap
    def dfs2(cur):
        m = len(g[cur])
        for nxt in g[cur]:
            ans[nxt] = ans[cur]+1+(cnt[cur]-1-cnt[nxt])/2
            yield dfs2(nxt)
        yield
    ans[0] = 1
    dfs2(0)
    print(*ans)
    return 


t = 1
# t = int(input())
import random
for i in range(t):
    solve()
    # print(i)
    # if solve():
    #     print("YES")
    # else:
    #     print("NO")
