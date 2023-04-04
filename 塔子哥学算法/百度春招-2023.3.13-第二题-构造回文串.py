
# 百度春招-2023.3.13-第二题-构造回文串
# 题目解析以及代码

# 关注公众号:塔子哥学算法，搜索“P1080”即可得到对应题解
# 题目内容

# 给定一个整数xx，请你构造一个仅由'r','e','d'三种字符组成的字符串，其中回文子串的数量恰好为xx

# 字符串的长度不得超过105105
# 输入描述

# 一个正整数xx.

# 1≤x≤1091≤x≤109
# 样例
# 输入

# 3

# 输出

# red

# 说明

# 输出"dd"也可以通过本题


from random import *
import sys
from collections import * 
from math import * 
from functools import *



def solve(n):
    def check(x):
        lo, hi = 1, x 
        while lo <= hi:
            mid = (lo+hi)//2
            if (mid+1)*mid//2 <= x:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi 
    ans = []
    while n:
        t = check(n)
        ans.append('d'*t)
        n -= (t+1)*t//2
        if n <= 3:
            ans.append('red'[:n])
            break 
        n -= 2
        ans.append('re')
    return ''.join(ans)

def verify(s):
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i+1,n+1):
            if s[i:j] == s[i:j][::-1]:
                # print(i,j,s[i:j])
                cnt += 1
    return cnt


def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for _ in range(1):
        # n, m, v, w = list(map(int,input().split()))
        n = int(input())
        # prizes = list(map(int,input().split()))
        # persons = list(map(int,input().split()))
        # n = randint(1,1000)
        # print(solve(n))
        s = solve(n)
        print(s)
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