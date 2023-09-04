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
# n = int(input())
# L, N1, N2 = list(map(int,input().split()))
s = input()

cc = Counter()
cc[0] = 1
ans = 0
cur = 0
for ch in s:
    ch = int(ch)
    cur ^= (1<<ch)
    ans += cc[cur]
    cc[cur] += 1
print(ans)