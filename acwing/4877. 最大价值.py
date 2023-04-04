# 有一个容量为 n 的背包和 m+1

# 种物品，每种物品都有无限多个。

# 物品种类编号为 0∼m

# 。

# 第 i
# 种物品的体积为 vi，价值为 wi

# 。

# 在使用背包装入物品时，每种物品的限重如下：

#     第 0

# 种物品：重量忽略不计，在装入时没有重量限制。
# 第 1∼m
# 种物品：第 i 种物品的单个重量为 hi，如果该种物品的装入总重量超过 li

#     ，则视为超重。

# 现在，请你挑选物品装入背包，要求

#     所有装入物品的总体积不得超过背包容量。
#     所有存在重量限制的物品均不得超重。
#     满足以上所有条件的前提下，所有装入物品的总价值尽可能大。

# 输出总价值的最大可能值。

# 注意审题，不要将 n,m

# 的含义弄混。
# 输入格式

# 第一行包含四个整数 n,m,v0,w0

# 。

# 接下来 m
# 行，每行包含四个整数 li,hi,vi,wi

# 。
# 输出格式

# 一个整数，表示总价值的最大可能值。
# 数据范围

# 前 4
# 个测试点满足 1≤n≤100，1≤m≤2。
# 所有测试点满足 1≤n≤1000，1≤m≤10，1≤li,hi,vi,wi≤100

# 。
# 输入样例1：

# 10 2 2 1
# 7 3 2 100
# 12 3 1 10

# 输出样例1：

# 241

# 输入样例2：

# 100 1 25 50
# 15 5 20 10

# 输出样例2：

# 200

# 难度： 中等
# 时/空限制： 1s / 256MB
# 总通过数： 773
# 总尝试数： 1835
# 来源： AcWing,第96场周赛
# 算法标签


from random import *
import sys
from collections import * 
from math import * 
from functools import *



def solve(n,m,vs,ws,cnts):
    @lru_cache(None)
    def dfs(i,v):
        if v < 0: return -inf 
        if i == 0: return (v//vs[0])*ws[0]
        ans = 0
        for j in range(cnts[i]+1):
            if v-j*vs[i] < 0: break 
            ans = max(ans, dfs(i-1,v-j*vs[i])+j*ws[i])
        return ans 

    return dfs(m,n)


def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for _ in range(1):
        n, m, v, w = list(map(int,input().split()))
        vs = [0]*(m+1)
        ws = [0]*(m+1)
        vs[0] = v 
        ws[0] = w 
        cnts = [0]*(m+1)
        for i in range(m):
            l,h,v,w = list(map(int,input().split()))
            vs[i+1] = v 
            ws[i+1] = w 
            cnts[i+1] = l//h 
        print(solve(n,m,vs,ws,cnts))
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