
# 2023.04.08-华为od-第一题-箱子之形摆放
# 题目内容

# 有一批箱子(形式为字符串，设为ss)，要求将这批箱子按从上到下以之形的顺序摆放在行数为n的空地，请输出箱子的摆放结果。

# 例如:箱子为ABCDEFG，空地的行数为3，摆放结果如图:

# image

# 所以输出:

# AFG

# BE

# CD
# 输入描述

# 第一行输入一个字符串ss和一个整数nn , 分别代表箱子和空地行数.

# 1.ss 只包含大写字母,1≤∣s∣≤10001≤∣s∣≤1000

# 2.1≤n≤10001≤n≤1000
# 输出描述

# 箱子摆放结果。如题目样例所示
# 样例

# 输入

# ABCDEFG 3

# 输出

# AFG
# BE
# CD

s,n = input().split()
n = int(n)
ans = [[] for _ in range(n)]
i = 0
di = 1
for ch in s:
    if i < 0:
        i = 0
        di = 1
    elif i >= n:
        i = n-1
        di = -1
    ans[i].append(ch)
    i += di 
for tmp in ans:
    print(''.join(tmp))