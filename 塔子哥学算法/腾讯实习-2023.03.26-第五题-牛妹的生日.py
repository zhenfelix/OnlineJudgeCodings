
# 腾讯实习-2023.03.26-第五题-牛妹的生日
# 题目内容

# 牛妹在生日这一天收到了一个长度为 nn 的序列 a1,a2,...,ana1​,a2​,...,an​。牛妹希望从这个序列中删除一些数,使得剩下的元素的最大公约数恰好等于 kk。

# 牛妹想知道有多少种删除的方宰。由于答室可能过大，请对 109+7109+7 取模

# 最大公约数:指两个或多个整数公有约数中最大的一个
# 输入描述

# 第一行输入两个正整数 n,kn,k

# 第二行输入 nn 个正整数代表 a1,a2,...,ana1​,a2​,...,an​

# 1⩽n,ai⩽1051⩽n,ai​⩽105
# 输出描述

# 输出一行整数，代表删除的方案数在109+7109+7 意义下的取值。
# 样例

# 输入

# 3 3
# 3 3 3

# 输出

# 7


from random import *
import sys
from collections import * 
from math import * 
from functools import *
from heapq import *



def solve(n,k,arr):
    mx = max(arr)
    cc = [0]*(mx+1)
    for a in arr: cc[a] += 1
    fs = [1]*(n+1)
    MOD = 10**9+7
    for i in range(1,n+1):
        fs[i] = (2*fs[i-1])%MOD 
    for i in range(k,mx+1):
        for j in range(i*2,mx+1,i):
            cc[i] += cc[j]
    dp = [0]*(mx+1)
    ans = 0
    for i in range(k,mx+1)[::-1]:
        dp[i] = fs[cc[i]]-1
        for j in range(i*2,mx+1,i):
            dp[i] -= dp[j]
        dp[i] %= MOD 
    return dp[k] 


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
        

if __name__ == "__main__":
    main()