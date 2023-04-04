
# 腾讯音乐-2023.3.23-第四题-调整字符串
# 题目内容

# 小红拿到了两个长度为n的、仅由小写字母组成的字符串s和t，她可以进行若干次操作:选择第一个字符串s的两个下标和i满足∣i−j∣=k∣i−j∣=k，交换si和sjsi​和sj​。 小红想知道，自己能否在有限次数的操作内,使得ss和tt相等?
# 输入描述

# 第一行输入一个正整数qq，代表询问次数。 每组询问输入三行：第一行是两个正整数n,kn,k,代表字符串的长度和交换字符的距离，接下来的两行分别输入一个长度为nn的、仅由小写字母组成的字符串，分别代表ss和tt。

# 100%的数据满足: 1≤q,n,k≤10001≤q,n,k≤1000
# 输出描述

# 对于每组询问，如果可以把ss变成tt，则输出”Yes"”Yes";否则输出"No""No"。
# 样例11

# 输入

# 2
# 2 1
# ab
# ba
# 3 2
# abc
# acb

# 输出

# Yes
# No
from random import *
import sys
from collections import * 
from math import * 
from functools import *



def solve(s,t,k):
    n = len(s)
    cc = [Counter() for _ in range(n)]
    for i in range(n):
        cc[i%k][s[i]] += 1
    for i in range(n):
        cc[i%k][t[i]] -= 1
        if cc[i%k][t[i]] < 0:
            return False
    
    return True


def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    case = int(input())
    for _ in range(case):
        n, k = list(map(int,input().split()))
        s = input()
        t = input()
        if solve(s,t,k):
            print("Yes")
        else:
            print("No")
    # a, b = list(map(int,input().split()))

    # for i in range(1000):
    #     b = randint(1,10000000)
    #     a = randint(1,b)
    #     assert(solve(a,b) == solve_another(a,b))
    #     print(i,a,b,'ok')

if __name__ == "__main__":
    main()