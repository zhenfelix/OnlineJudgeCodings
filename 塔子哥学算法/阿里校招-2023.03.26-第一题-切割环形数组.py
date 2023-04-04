
# 阿里校招-2023.03.26-第一题-切割环形数组
# 题目内容

# 给定一个环形数组，你需要切两刀，把它切成两段，使得两段的元素之和相等。请问有多少种切割方案？
# 输入描述

# 第一行输入一个正整数 nn ，代表环形数组的元素数量。

# 第二行输入 nn 个正整数 aiai​，代表环形数组的元素。

# 1≤n≤1051≤n≤105

# −109≤ai≤109−109≤ai​≤109
# 输出描述

# 一个整数，代表切割的方案数。
# 样例

# 输入

# 4
# 1 2 -1 2

# 输出

# 2


from random import *
import sys
from collections import * 
from math import * 
from functools import *



def solve(n,arr):
    tot = sum(arr)
    if tot%2: return 0
    cc = Counter()
    cc[0] = 0
    s, ans = 0, 0
    for a in arr:
        s += a 
        ans += cc[s-tot//2]
        cc[s] += 1
    return ans 

def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for _ in range(1):
        # n, m = list(map(int,input().split()))
        n = int(input())
        arr = list(map(int,input().split()))
        # brr = list(map(int,input().split()))
        # s = input()
        # prizes = list(map(int,input().split()))
        # persons = list(map(int,input().split()))
        # n = randint(1,1000)
        print(solve(n,arr))
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