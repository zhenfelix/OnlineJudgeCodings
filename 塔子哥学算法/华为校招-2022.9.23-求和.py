
# 华为校招-2022.9.23-求和
# 题目解析以及代码

# 关注公众号:塔子哥学算法，搜索“P1004”即可得到对应题解
# 求和

# (华为-校招-算法-9.23)
# 题目大意

# 给定一个大小为n的数组，请问存在多少中方案的子序列使得改子序列的和是原数组元素总和的一半。
# 样例输入

# 输入

# 7
# 1 2 3 4 5 6 7

# 输出

# 8

# 数据范围

# 1≤n≤2001≤n≤200 数组元素大于0且其总和不超过 1e51e5 , 保证方案总数不超过int的最大值。


from random import *
import sys
from collections import * 
from math import * 
from functools import *



def solve(arr):
    tot = sum(arr)
    n = len(arr)
    @lru_cache(None)
    def dfs(i,s):
        if s < 0: return 0
        if s == 0: return 1
        if i < 0: return 0
        return dfs(i-1,s)+dfs(i-1,s-arr[i])
    if tot%2: return 0
    return dfs(n-1,tot//2)


def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for _ in range(1):
        # n, m, v, w = list(map(int,input().split()))
        n = int(input())
        arr = list(map(int,input().split()))
        print(solve(arr))
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