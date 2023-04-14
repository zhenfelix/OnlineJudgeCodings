
// 2023.03.21-第三题-数数
// 题目内容

// 塔子哥是一个数学家，他喜欢研究各种数学问题。有一天，他在数数时想到了这个问题。给定一个正整数序列，从前往后进行数数: 1,2,3,4,5,6,7,8,9,10,11,…。

// 试求当塔子哥数到多少时，0到9每个数字各出现了至少 kk 次。

// 其中，我们定义“数字”为十进制下的数位，例如，3233出现了三个’3’和一个2。

// 共有 tt 组询问，每组询问都是独立的。
// 输入描述

// 第一行输入一个正整数tt，代表询问的次数。 接下来的tt行，每行输入一个正整数kk，代表一次询问。

// 1≤t≤1000,1≤k≤10131≤t≤1000,1≤k≤1013
// 输出描述

// 输出tt行，每行输出一个整数，代表每次询问的答案。
// 样例11

// 输入

// 3
// 1
// 2
// 3

// 输出

// 10
// 20
// 30

// 说明： 在第1组询问中，当数到10时，0到9每个数至少出现了1次。

import sys 
from functools import *

# sys.stdin = open("contests/input","r")
t = int(input())

for _ in range(t):
    k = int(input())
    
    lo, hi = 1, 10*k
    while lo <= hi:
        x = (lo+hi)//2
        s = list(map(int,list(str(x))))
        n = len(s)

        @lru_cache(None)
        def dfs(i,fhi,zero,cnt,target):
            if i == n: return cnt 
            hi = s[i] if fhi else 9 
            res = 0
            if hi > 0:
                res += (hi-1)*dfs(i+1,False, False, 
        cnt, 
        target)
                res += dfs(i+1,fhi, False, 
        cnt, 
        target)
            res += dfs(i+1, fhi and 0 == hi, zero, 
        cnt+(not zero), 
        target)
            return res 
        
        # print(x,dfs(0,True,True,0,x))
        if dfs(0,True,True,0,x) < k:
            
            lo = x+1
        else:
            hi = x-1
    print(lo)
    
    
    
    
    
    
    
    
    

    
