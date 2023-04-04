
# 腾讯实习-2023.03.26-第四题-子数组异或和
# 题目内容

# 给出一个正整数数组 AA，牛牛想知道其中有多少子数组满足: 里面所有数字的乘积等于里面所有数字的异或。

# 一个数组的子数组指数组中非空的一段连续数字
# 输入描述

# 第一行一个正整数 nn，代表给出数组长度

# 第二行 nn 个空格分隔的正整数 AA;

# 1⩽n⩽1051⩽n⩽105

# 1⩽Ai⩽1091⩽Ai​⩽109
# 输出描述

# 输出一个正整数代表答案
# 样例

# 输入

# 3
# 1 2 1

# 输出

# 4

# 样例解释

# 数组 [1],[2],[1],[1,2,1][1],[2],[1],[1,2,1] 都是满足条件的。


from random import *
import sys
from collections import * 
from math import * 
from functools import *
from heapq import *



def solve(n,arr):
    st = [-1]
    arr.append(None)
    l, s = 1, 1
    INT_MAX = (1<<32)-1
    ans = 0
    for i in range(n):
        if arr[i] > 1:
            st.append(i)
        s *= arr[i]
        while s > INT_MAX:
            s //= arr[st[l]]
            l += 1
        mul, xor = 1, 0
        if arr[i] == 1:
            xor = (i-st[-1])&1
            ans += (i-st[-1]+1)//2
        for j in range(l,len(st))[::-1]:
            mul *= arr[st[j]]
            xor ^= arr[st[j]]
            ones = st[j]-st[j-1]-1
            if mul == xor:
                ans += ones//2+1
            if mul == (xor^1):
                ans += (ones+1)//2
    return ans 


def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for _ in range(1):
        # n, k = list(map(int,input().split()))
        n = int(input())
        arr = list(map(int,input().split()))
        # brr = list(map(int,input().split()))
        # s = input()
        # prizes = list(map(int,input().split()))
        # persons = list(map(int,input().split()))
        # n = randint(1,1000)
        print(solve(n,arr))
        

if __name__ == "__main__":
    main()