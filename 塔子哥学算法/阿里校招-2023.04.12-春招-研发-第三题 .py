# 题目内容

# 曾经有一个小镇叫做“数字王国”，这个小镇以数字相关的工艺和技术而闻名于世。其中最出名的数字工匠就是塔子哥。他被认为是数字领域中最聪明的人之一。他的天赋是发现数字之间的规律，并创造一些有趣的数字游戏。

# 其中一天，塔子哥想出了一个游戏：删除数字。这个游戏的规则是：给定一个正整数，你需要删除其中连续的一段数字，使得它变成15的倍数。他想知道有多少种不同的删除方式可以达到这个目标。

# 现在，他把这个问题交给了你。

# 注：删除的位置不同，即可记为两种不同的方式，并且允许删除后的数存在前导零。同时,不能全删也不能不删
# 输入描述

# 输入一个正整数 nn 。 1≤n≤101000001≤n≤10100000
# 输出描述

# 一个正整数，代表删除的方案数。
# 样例

# 输入

# 12313565

# 输出

# 9





# 塔子哥测试数据里面有字符串末尾可能有new line，导致python直接读取input会runtime error，需要input().strip()才能运行


def solve(s):
    n = len(s)
    dp = [0]
    MOD = 15
    cc = [0]*MOD 
    cc[0] += 1
    for ch in s:
        a = int(ch)
        dp.append((dp[-1]*10+a)%MOD)
        cc[dp[-1]] += 1
    ans = 0
    r2, base = 0, 1
    for i in range(n)[::-1]:
        cc[dp[i+1]] -= 1
        for r1 in range(MOD):
            if (r1*base+r2)%MOD == 0:
                ans += cc[r1]
        r2 = (r2+base*int(s[i]))%MOD
        base = (base*10)%MOD 
    # print(ans-1)
    return ans-1

def brute(s):
    n = len(s)
    ans = 0
    MOD = 15
    for j in range(n)[::-1]:
        left = '0'
        right = s[j+1:]
        if int(left+right)%MOD == 0:
            ans += 1
        for i in range(j):
            left += s[i]
            if int(left+right)%MOD == 0:
                ans += 1
    return ans-1

# s = input().strip()
s = "12313565"
res1 = solve(s)
res2 = brute(s)
assert(res1 == res2)

import random
t = 10
for _ in range(t):
    n = random.randint(5,1000)
    s = ''.join([str(random.randint(0,9)) for _ in range(n)])
    res1 = solve(s)
    res2 = brute(s)
    assert(res1 == res2)