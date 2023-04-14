# 塔子哥之前的种植的白菜，最近到了收获的季节，为了让收获的白菜口感又好，又嫩。所以塔子哥要估计白菜的大概长度，后面再来一波机械化收割。

# 假设一批白菜的平均长度服从密度函数为 sin(x)/5.68sin(x

# ​)/5.68 的分布，其中平均长度 xx 个于 [1,10][1,10] 之间。

# 塔子哥想知道介于 [a,b]⊂[1,10][a,b]⊂[1,10] 的概率是否大于 0.50.5 以方便收割最大化。

# 我们知道通过数值积分可以给出 P(a≤X≤b)=∫basin(x)/5.68≈∑i=0n−1sin(xi)/5.68ΔxP(a≤X≤b)=∫ba​sin(x
# ​)/5.68≈∑i=0n−1​sin(xi​

# ​)/5.68Δx

# 其中 a=x0<x1<...<xn=ba=x0​<x1​<...<xn​=b and xi+1−xi=Δxand xi+1​−xi​=Δx ，取 n=500n=500 ，相当于把区间 [a,b][a,b] 分成 500500 份。
# 输入描述

# 第 11 行表示测试数据组数 TT

# 接下来的 TT 行，每一行表示输入 aa ， bb ， 1≤a<b≤101≤a<b≤10 表示范围。
# 输出描述

# 输出 11 或者 00 ，如果得到的概率大于 0.50.5 则输出 11 否则则输出 00 。
# 样例

# 输入

# 4
# 3 7
# 5 6
# 2 9
# 8 9

# 输出

# 1
# 0
# 1
# 0

from math import *
def calc(a,b):
    delta = (b-a)/500
    ans = 0
    x = a + delta
    for _ in range(500):
        ans += delta*sin(sqrt(x))/5.68
        x += delta  
    return ans 

t = int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    if calc(a,b) > 0.5:
        print(1)
    else:
        print(0)