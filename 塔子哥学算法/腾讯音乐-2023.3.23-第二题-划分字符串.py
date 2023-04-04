
# 腾讯音乐-2023.3.23-第二题-划分字符串
# 题目内容

# 小红定义一个字符串的权值为：字符串长度乘以字符串的字母种类数量。例如，"abacb""abacb"的价值为5∗3=155∗3=15。 小红拿到了一个字符串，她准备将该字符串切分成kk个子串 (将这个子串按顺序拼在一起即可得到原串》。小红希望切分后这人个子串的最大权值尽可能小。你能帮帮小红吗?你不需要给出一个方案，只需要返回最终这kk个子串的最大权值即可。字符串仅包含小写字母，且长度不超过500000500000。kk为不超过字符串长度的正整数。
# 样例11

# 输入

# ababbbb
# 2

# 输出

# 6

# 说明 将字符串切分成"aba""aba"和"bbbb""bbbb"，第一段的权值为6，第二段的权值为4，权值最大值为6。可以证明，这样切分得到的答案是最小的。

from random import *
import sys
from collections import * 
from math import * 
from functools import *



def solve(s,k):
    n = len(s)
    lo, hi = 1, n*n 
    def check(t):
        cnt = 1
        sz, visited = 0, set()
        for ch in s:
            sz += 1
            visited.add(ch)
            if len(visited)*sz > t:
                visited = set([ch])
                sz = 1
                cnt += 1
            if cnt > k:
                return False
        return True 
    while lo <= hi:
        mid = (lo+hi)//2
        if check(mid):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo 
    
    return cntb


def main():
    # sys.stdin = open('contests/input', 'r')
    s = input()
    k = int(input())
    # a, b = list(map(int,input().split()))
    print(solve(s,k))

    # for i in range(1000):
    #     b = randint(1,10000000)
    #     a = randint(1,b)
    #     assert(solve(a,b) == solve_another(a,b))
    #     print(i,a,b,'ok')

if __name__ == "__main__":
    main()