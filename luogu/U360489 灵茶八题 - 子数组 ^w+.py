https://www.luogu.com.cn/blog/endlesscheng/post-ling-cha-ba-ti-ti-mu-lie-biao

import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType
from math import *

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
# n, m = list(map(int,input().split()))
# arr = []
# for _ in range(n):
#     arr.append(list(map(int,input().split())))
arr = list(map(int,input().split()))
# crr = list(map(int,input().split()))

# n = int(input())
# L, N1, N2 = list(map(int,input().split()))
MOD = 10**9+7
def solve():
    ans = 0
    base = 1
    for _ in range(22):
        cur = 0
        cnt = [1,0]
        s = 0
        for i in range(n):
            cur ^= (arr[i]&1)
            arr[i] >>= 1
            s += cnt[cur^1]
            cnt[cur] += 1
        ans += s*base 
        base <<= 1
    return ans 

print(solve())