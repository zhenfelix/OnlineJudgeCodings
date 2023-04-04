# 给定一个长度为 n 的整数序列 d1,d2,…,dn 以及三个整数 k,a,b

# 。

# 初始时，所有 di
# 均为 0

# 。

# 你需要对序列依次进行 q

# 次操作，操作分为以下两种：

#     1 x y，将 dx

# 增加 y
# 。
# 2 p，计算并输出 ∑i=1p−1min(di,b)+∑i=p+knmin(di,a)

#     。

# 输入格式

# 第一行包含 5
# 个整数 n,k,a,b,q

# 。

# 接下来 q

# 行，每行描述一个操作，格式如题面所述。
# 输出格式

# 每个 2 p 操作，输出一行一个整数表示结果。
# 数据范围

# 前 3
# 个测试点满足 1≤k≤n≤10，1≤q≤10。
# 所有测试点满足 1≤k≤n≤2×105，1≤b<a≤10000，1≤q≤2×105，1≤x≤n，1≤y≤10000，1≤p≤n−k+1

# 。
# 输入样例1：

# 5 2 2 1 8
# 1 1 2
# 1 5 3
# 1 2 1
# 2 2
# 1 4 2
# 1 3 2
# 2 1
# 2 3

# 输出样例1：

# 3
# 6
# 4

# 输入样例2：

# 5 4 10 1 6
# 1 1 5
# 1 5 5
# 1 3 2
# 1 5 2
# 2 1
# 2 2

# 输出样例2：

# 7
# 1

# 难度： 困难
# 时/空限制： 1s / 256MB
# 总通过数： 284
# 总尝试数： 896
# 来源： AcWing,第96场周赛
# 算法标签
from random import *
import sys
from collections import * 
from math import * 
from functools import *



def solve():
    n, k, a, b, q = list(map(int,input().split()))
    nmax = n+10
    treea = [0]*nmax
    treeb = [0]*nmax
    arr = [0]*(n+1)
    def update(tree, i, v):
        while i <= nmax:
            tree[i] += v 
            i += (i&-i)
        return 
    def query(tree, i):
        res = 0
        while i:
            res += tree[i]
            i -= (i&-i)
        return res 

    for _ in range(q):
        ops = list(map(int,input().split()))
        if len(ops) == 3:
            _, x, y = ops
            update(treea,x,min(y,max(0,a-arr[x])))
            update(treeb,x,min(y,max(0,b-arr[x])))
            arr[x] += y 
        else:
            _, p = ops
            l = query(treeb, p-1)
            r = 0
            if p+k <= n:
                r = query(treea, n)-query(treea, p+k-1)
            print(l+r)


    return 


def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for _ in range(1):
        # n, m, v, w = list(map(int,input().split()))
        solve()
        # print(solve(n,m,vs,ws,cnts))
        # if solve(n,l,r):
        #     print("Yes")
        # else:
        #     print("No")
    # a, b = list(map(int,input().split()))

    # for i in range(1000):
    #     b = randint(1,10000000)
    #     a = randint(1,b)
    #     assert(solve(a,b) == solve_another(a,b))
    #     print(i,a,b,'ok')

if __name__ == "__main__":
    main()