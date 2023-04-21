# 题目内容

# 塔子哥参加ACM竞赛的过程中遇到过各种各样的计数题。唯独二进制计数题他整不明白。这不，今天WZ银行恰好又出了一道这种题，他还是依旧大脑空白。你可以帮助他吗？

# 塔子哥拿到了四个非负整数LL,RR,XX,YY，请计算有多少个非负整数NN满足以下四个条件：

# 1.NN的二进制表示中1的个数不小于LL

# 2.NN的二进制表示中1的个数不大于RR

# 3.NN和XX的按位与为XX

# 4.NN和YY的按位或为YY
# 输入描述

# 第一行有一个正整数TT(1≤T≤10001≤T≤1000)，代表有多少组测试数据。接下来是TT组测试数据，每组由一行构成。

# 每一组测试数据仅包含四个整数L,R,X,YL,R,X,Y (0≤L≤R≤30,0≤X,Y≤230−10≤L≤R≤30,0≤X,Y≤230−1)
# 输出描述

# TT行，每行输出一个整数，代表你求得的答案。
# 样例
# 样例1

# 输入

# 1
# 2 4 1 3

# 输出

# 1

# 样例2

# 输入

# 2
# 2 3 8 62
# 3 5 20 61

# 输出

# 10
# 7


from math import comb
t=int(input())
def solve(l,r,x,y):
    ones,zeros,f = 0,0,0
    while x or y:
        if (x&1) == 1 and (y&1) == 0:
            return 0
        if (x&1) == 1:
            ones += 1
        elif (y&1) == 0:
            zeros += 1
        else:
            f += 1
        x >>= 1
        y >>= 1
    ans = 0
    for i in range(l,r+1):
        if i-ones <= f:
            ans += comb(f,i-ones)
    return ans
for _ in range(t):
    l,r,x,y = list(map(int,input().split()))
    print(solve(l,r,x,y))