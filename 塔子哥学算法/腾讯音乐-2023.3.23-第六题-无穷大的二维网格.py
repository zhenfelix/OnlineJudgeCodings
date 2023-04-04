
# 腾讯音乐-2023.3.23-第六题-无穷大的二维网格
# 题目内容

# 有一个无穷大的二维网格图，一开始所有格子都未染色。给你一个正整数 n，表示你需要执行以下步骤 n 分钟: 第一分钟，将任一格子染成蓝色。之后的每一分钟，将与蓝色格子相邻的 所有未染色格子染成蓝色。 小红在第n分钟时，发现已经染色了n * n + (n -1) * (n -1)个格子。她准备按从上到下、从左到右的顺序为每个格子进行编号 (下图分别代表第1、2、3分钟时每个格子的编号情况)。小红想知道，第n分钟，ll编号和rr编号的曼哈顿距离是多少? 在这里插入图片描述

# 注: 曼哈顿距离指横向距离和纵向距离之和例如n = 3时，5号格子和13号格子的曼哈顿距离为2+2=4。
# 输入描述

# 第一行输入一个正整数tt，代表询问次数。接下来的t行，每行输入三个正整数n,l,rn,l,r，代表一次询问。 1≤t≤1041≤t≤104 1≤n≤1081≤n≤108 1≤l≤r≤n∗n+(n−1)∗(n−1)1≤l≤r≤n∗n+(n−1)∗(n−1)
# 输出描述

# 输出tt行，每行输入一个整数，代表该次询问的答案。
# 样例11

# 输入

# 2
# 3 5 13
# 2 1 3

# 输出

# 4
# 1



from random import *
import sys
from collections import * 
from math import * 
from functools import *



def solve(n,l,r):
    def calc(target):
        lo, hi = 1, n 
        while lo <= hi:
            mid = (lo+hi)//2
            if target <= mid*mid:
                hi = mid-1
            else:
                lo = mid+1
        return (lo-(lo*lo-target)-1,n-lo)
    def pos(target):
        if target <= n*n:
            return calc(target)
        tot = n*n+(n-1)*(n-1)
        x, y = calc(tot+1-target)
        return (-x,-y)
    x1, y1 = pos(l)
    x2, y2 = pos(r)
    return abs(x1-x2)+abs(y1-y2)
    
    return True


def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    case = int(input())
    for _ in range(case):
        n, l, r = list(map(int,input().split()))
        print(solve(n,l,r))
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