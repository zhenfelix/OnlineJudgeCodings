
# 阿里校招-2023.03.26-第二题-报数字
# 题目内容

# nn 个学生围成一圈，编号从1到 nn 。

# 每个学生将从1开始报数，报到素数的人出列，剩下的人继续报数。试求最终留下来的人的编号是多少。
# 输入描述

# 一个正整数n。代表学生的人数。

# 1≤n≤1041≤n≤104
# 输出描述

# 一个正整数，代表最终留下来的学生编号。
# 样例
# 样例 1

# 输入

# 4

# 输出

# 4

# 样例解释

# 报数流程如下：

# 1号报1。

# 2号报2，出队。

# 3号报3，出队。

# 4号报4。

# 1号报5，出队。

# 最后留下来的是4号
# 样例 2

# 输入

# 6

# 输出

# 4


from random import *
import sys
from collections import * 
from math import * 
from functools import *
from heapq import *



def solve(n):
    mx = 10**5+10**4

    f = [1]*mx
    f[0] = 0
    for i in range(2,mx):
        if f[i] == 0: continue
        for j in range(i*i,mx,i):
            f[j] = 0 
    primes = [i for i in range(mx) if f[i]]
    def query(tree, x):
        r = 0
        while x: 
            r += tree[x]
            x -= (x&-x)
        return r 
    def update(tree, x, delta):
        while x < len(tree):
            tree[x] += delta
            x += (x&-x)
        return 
    arr = [0]*(n+1)
    for i in range(1,n+1):
        update(arr,i,1)
    cnt = n
    pre = cur = 1
    def search(lo,hi,v):
        while lo <= hi:
            mid = (lo+hi)//2
            if query(arr,mid) < v:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    def check(x):
        x = (x-1)%cnt + 1
        base = query(arr, pre)
        if x+base <= cnt:
            return search(pre,n,x+base)
        else:
            return search(1,pre,x+base-cnt)
    for i in range(1,n+1):
        cur = check(primes[i]-primes[i-1])
        update(arr,cur,-1)
        cnt -= 1
        pre = cur 

    return cur   

def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for _ in range(1):
        # n, k = list(map(int,input().split()))
        n = int(input())
        # arr = list(map(int,input().split()))
        # brr = list(map(int,input().split()))
        # s = input()
        # prizes = list(map(int,input().split()))
        # persons = list(map(int,input().split()))
        # n = randint(1,1000)
        print(solve(n))
        

if __name__ == "__main__":
    main()