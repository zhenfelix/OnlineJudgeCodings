# 题目内容

# 塔子哥是一名热爱字符串算法的程序员。他最近遇到了一个有趣的问题。

# 给定一个字符串 ss，字符串中包含多少个 red 子串，就给这个字符串一个权值，权值就是 red 子串的数量。

# 例如:reddredd 权值为1，redredrredredr 权值为2,reedreed 权值为0

# 现在考虑计算一个字符串 ss 所有非空子序列的权值和。 答案可能很大，请对1e9+71e9+7取模

#     长为 nn 的字符串的非空子序列为 2n−12n−1 个。

# 输入描述

# 输入第一行为一个字符串s(1≤∣s∣≤100000)s(1≤∣s∣≤100000)。
# 输出描述

# 输出字符串所有非空子字符串的权值和。
# 样例

# 输入

# rredd

# 输出

# 9


import sys 
# sys.stdin = open("contests/input","r")

s=input() 
n = len(s)
MOD = 10**9+7 
fs =[1]*(n+1)
for i in range(n):
    fs[i+1] = fs[i]*2 
    fs[i+1] %=MOD 
r,d,cur=0,0,0
for i in range(n):
    if s[i] == 'd': d+=fs[n-i-1]
ans = 0

for i, ch in enumerate(s):
    if ch == 'r':
        r += fs[i] 
        cur += fs[i]*d 
        r %= MOD 
        cur %= MOD 
    elif ch == 'd':
        d -= fs[n-i-1] 
        cur -= fs[n-i-1]*r 
        d %= MOD 
        cur %= MOD 
    else:
        ans += cur 
        ans %= MOD 
print(ans)