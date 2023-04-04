
# 字节春招后端-2023.03.24-第二题-摇骰子
# 题目解析以及代码

# 关注公众号:塔子哥学算法，搜索“P1113”即可得到对应题解
# 题目内容

# 小明和小红在玩摇骰子游戏，每个骰子有固定的面数 k (2⩽k⩽8)k (2⩽k⩽8)，每一面对应的点数分别为 1,2,…,k1,2,…,k。

# 小明有 n (1⩽n⩽20)n (1⩽n⩽20) 个骰子，对于骰子 i (1⩽i⩽n)i (1⩽i⩽n)，它的面数为 ai (2⩽ai⩽8)ai​ (2⩽ai​⩽8)，摇到每一面的概率都是 1aiai​1​。小红有 m (1⩽m⩽20) m (1⩽m⩽20) 个骰子，对于骰子 j (1⩽j⩽m)j (1⩽j⩽m)，它的面数为 bj (2⩽bj⩽8)bj​ (2⩽bj​⩽8)，摇到每一面的概率都是 1bibi​1​。

# 小明和小红分别摇各自拥有的全部骰子，然后把骰子朝上那一面的点数相加，最后比较谁的点数和最大，大的获胜，相同平手，小的获败。小明和小红只摇一把，平手不会继续重摇，小明想知道他获胜的概率，你能帮帮他吗？
# 输入描述

# 共三行，第一行包含两个正整数 nn 和 mm ，

# 第二行包含 nn 个整数，表示 a0,a1,…,an−1a0​,a1​,…,an−1​，

# 第三行包含 mm 个整数，表示 b0,b1,…,bm−1b0​,b1​,…,bm−1​。
# 输出描述

# 共一行，一个浮点数，表示小明获胜的概率，保留小数点后3位有效数字。
# 样例

# 输入

# 1 3
# 8
# 2 3 4

# 输出

# 0.255   

# 说明

# 100%的数据：1⩽n,m⩽20, 2⩽ai,bi⩽81⩽n,m⩽20, 2⩽ai​,bi​⩽8。


from random import *
import sys
from collections import * 
from math import * 
from functools import *



def solve(arr,brr):
    nmax = 170
    def calc(ps):
        dp = [0]*nmax
        dp[0] = 1
        for p in ps:
            for i in range(nmax)[::-1]:
                dp[i] = sum(dp[i-j]/p for j in range(1,p+1) if i >= j)
        return dp 
    ans = 0
    c = 0
    pa, pb = calc(arr), calc(brr)
    for i in range(nmax):
        ans += c*pa[i]
        c += pb[i]

    return ans 

def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for _ in range(1):
        n, m = list(map(int,input().split()))
        # n = int(input())
        arr = list(map(int,input().split()))
        brr = list(map(int,input().split()))
        
        # prizes = list(map(int,input().split()))
        # persons = list(map(int,input().split()))
        # n = randint(1,1000)
        # print(solve(n))
        s = solve(arr,brr)
        print(f'{round(s,3):.3f}')
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