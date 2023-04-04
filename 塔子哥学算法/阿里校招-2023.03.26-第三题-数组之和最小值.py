
# 阿里校招-2023.03.26-第三题-数组之和最小值
# 题目内容

# 给定一个数组，你可以进行最多k次以下操作：

# 选择一个大于1的元素 aiai​ ，使得 aiai​ 除以它的一个素因子pp。

# 试求操作结束后，数组的所有元素之和的最小值是多少？
# 输入描述

# 第一行输入两个正整数nn和kk，代表数组大小以及操作次数。

# 第二行输入nn个正整数aiai​，代表数组的元素。

# 1≤n,k≤2000001≤n,k≤200000

# 1≤ai≤1061≤ai​≤106
# 输出描述

# 一个整数，代表操作后的所有元素最小的和。
# 样例

# 输入

# 2 1
# 5 6

# 输出

# 7

# 样例解释

# 只能操作一次，选择一个元素，5／5＝1即可，数组变成[1,6]。


from random import *
import sys
from collections import * 
from math import * 
from functools import *
from heapq import *



def solve(n,k,arr):
    mx = max(arr)
    tot = sum(arr)
    f = list(range(mx+1))
    for i in range(2,mx+1):
        if f[i] != i: continue
        for j in range(i*2,mx+1,i):
            f[j] = i 
    hq = []
    for a in arr:
        while a > 1:
            hq.append(a//f[a]-a)
            a //= f[a]
    heapify(hq)
    for _ in range(k):
        if not hq: break 
        tot += heappop(hq)
    return tot  

def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for _ in range(1):
        n, k = list(map(int,input().split()))
        # n = int(input())
        arr = list(map(int,input().split()))
        # brr = list(map(int,input().split()))
        # s = input()
        # prizes = list(map(int,input().split()))
        # persons = list(map(int,input().split()))
        # n = randint(1,1000)
        print(solve(n,k,arr))
        # ans = solve(s)
        # print(f'{round(ans,3):.3f}')
        # print(f'{0.0:.3f}')
        # m = verify(s)
        # assert(m == n)
        # print(n,s,'ok')
        # print(get_num_without_prize(persons, prizes))
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