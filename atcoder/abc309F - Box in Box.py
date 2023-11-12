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
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
# arr = list(map(int,input().split()))
# n = int(input())
# L, N1, N2 = list(map(int,input().split()))

def solve():
    global arr
    arr = [sorted(a) for a in arr]
    arr = sorted(arr, key=lambda x: (x[0],-x[1]))
    mp = {v: i+1 for i, v in enumerate(sorted([a[1] for a in arr]))}
    tree = [inf]*(n+10)
    def query(idx):
        mx = inf 
        while idx:
            mx = min(mx, tree[idx])
            idx -= idx&-idx 
        return mx 
    def update(idx, a):
        while idx < len(tree):
            tree[idx] = min(tree[idx], a)
            idx += idx&-idx 
        return 
    for a in arr:
        x, h = a[1:]
        x = mp[x]
        if query(x-1) < h:
            return True
        update(x,h)
    return False


if solve():
    print("Yes")
else:
    print("No")



请先阅读：
【图解】算法优化+详细证明 

接着上面的题解说。对于每个盒子，把长宽高从小到大排序（排序后分别记作 a[i][0], a[i][1], a[i][2]），然后按照 a[i][0] 从小到大排序所有盒子。

接下来只需要考虑是否有 a[i][1] < a[j][1] 且 a[i][2] < a[j][2]，这可以用树状数组解决（数据范围太大可以用离散化或者哈希表实现）。
把 (a[i][1], a[i][2]) 看成是二维平面的坐标点，我们可以维护 x=a[i][1] 这条线左侧的所有坐标点的纵坐标的最小值，即前缀最小值 preMin(a[i][1]-1)。
只要满足 preMin(a[i][1]-1) < a[i][2] 就可以输出 Yes。
具体细节见代码，注意为了满足严格小于，对于相同的 a[i][0] 需要先查询完再一并更新。

https://atcoder.jp/contests/abc309/submissions/45242148
