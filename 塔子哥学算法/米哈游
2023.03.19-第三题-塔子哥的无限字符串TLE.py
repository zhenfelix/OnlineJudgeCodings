
# 2023.03.19-第三题-塔子哥的无限字符串
# 题目内容

# 在某个神秘的数字世界中，有一位数学家塔子哥。他是这个数字世界中最聪明的人，他喜欢研究各种数字规律。

# 今天，塔子哥得到了一个无限长的字符串，该字符串代表着整个自然数集。这个字符串由数字字符 , 和 ; 以及数字组成，其中每三个数字由一个分号隔开，其它的数字由逗号隔开。

# 具体字符串为：1,2,3;4,5,6;7,8,9;10,11,12;13,14...... 。

# 塔子哥对这个字符串产生了浓厚的兴趣，并想知道该字符串的第 ll 个字符到第 rr 个字符之间有多少个逗号和分号。
# 输入描述

# 第一行输入一个正整数 tt ，代表询问次数。

# 接下来的 tt 行，每行输入两个正整数 ll 和 rr ，代表一次询问。

# 1≤t≤1041≤t≤104

# 1≤l≤r≤10121≤l≤r≤1012
# 输出描述

# 输出 tt 行，每行输入两个整数，用空格隔开。

# 分别代表 , 的数量和 ; 的数量。
# 样例

# 输入

# 2
# 3 6
# 8 10

# 输出

# 1 1
# 2 0

# 样例解释

# 第 33 个字符到第 66 个字符是 "2，3;" ，包含一个逗号和一个分号。

# 第 88 个字符到第 1010 个字符是 ”，5，" ，包含 22 个逗号，没有分号。

import sys
from collections import *
from functools import lru_cache


def calc(m):
    s = list(map(int,list(str(m))))
    n = len(s)
    @lru_cache(None)
    def dfs(i,zero,fhi):
        if i == n:
            return 0, 1
        hi = s[i] if fhi else 9
        sums, cnt = 0, 0
        candidates = [(0,1)] if hi == 0 else [(0,1),(-1,hi-1),(hi,1)]
        for ch, mutiples in candidates:
            sums_, cnt_ = dfs(i+1,zero and ch == 
    0, fhi and 
    ch == hi)
            sums += sums_*mutiples
            cnt += cnt_ *mutiples
            if zero and ch == 0: continue
            sums += cnt_ *mutiples
        return sums, cnt 
    # dfs.cache_clear()
    return dfs(0,1,1)[0]
    


def solve(l,r):
    
    def check(target):
        lo, hi = 1, target
        while lo <= hi:
            m = (lo+hi)//2
            if calc(m)+m >= target:
                hi = m-1
            else:
                lo = m+1
        return lo 
    left, right = check(l), check(r)

    flag = (calc(right)+right == r)
    ans = [0,0]
    k = (right-left)//3
    ans[0] += 2*k 
    ans[1] += k 
    symbols = [1,0,0]
    left += k*3
    for i in range(left,right+1):
        ans[symbols[i%3]] += 1
        if i == right and flag == 0:
            ans[symbols[i%3]] -= 1
    # print(*ans)
    return tuple(ans)

def brute(l,r):
    cur = 1
    rank = 0
    symbols = [1,0,0]
    res =[0,0]
    while rank <= r:
        rank += len(str(cur))+1
        if l <= rank <= r:
            res[symbols[cur%3]] += 1
        cur += 1
    return tuple(res)


from random import *
# sys.stdin = open("contests/input","r")
t = int(input())
# t = 100
for _ in range(t):
    l, r = list(map(int,input().split()))
    print(*solve(l,r))
    # l, r = randint(1,10000000000), randint(1,1000000000000)
    # if l > r: l, r = r, l 
    # res1 = solve(l,r)
    # res2 = brute(l,r)
    # print(l,r,res1,res2)
    # assert(res1 == res2)