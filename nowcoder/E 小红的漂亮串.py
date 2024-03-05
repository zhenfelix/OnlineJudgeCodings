# 链接：https://ac.nowcoder.com/acm/contest/69695/E
# 来源：牛客网

# 题目描述
# 小红定义“漂亮串”为：至少包含一个"red"子串，且不能包含"der"子串。例如"redced"为漂亮串，但"reder"则不是漂亮串。
# 小红想知道，长度为 nn 的、仅包含小写字母的字符串中，共有多少种不同的漂亮串？
# 输入描述:

# 一个正整数 nn，代表数组的长度。
# 1≤n≤1051≤n≤105

# 输出描述:

# 长度为 nn 的，漂亮串的种类数。答案对 109+7109+7 取模。

# 示例1
# 输入
# 复制

# 3

# 输出
# 复制

# 1

# 说明

# 仅有"red"这一个漂亮串

# 示例2
# 输入
# 复制

# 4

# 输出
# 复制

# 52

import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
lii = lambda: list(map(int, input().split()))

MOD = 10**9+7

def solve():
    n = ii()
    if n < 3:
        return 0
    # 不含der
    dp = [1, 0, 0]  # x, d, de
    for _ in range(n):
        tmp = [0, 0, 0]
        tmp[0] = (dp[0]*25 + dp[1]*24 + dp[2]*24) % MOD
        tmp[1] = (dp[0] + dp[1] + dp[2]) % MOD
        tmp[2] = dp[1]
        dp = tmp
    der = sum(dp) % MOD
    
    # 不含der和red
    dp = [1, 0, 0, 0, 0]  # x, d, de, r, re
    for _ in range(n):
        tmp = [0] * 5
        tmp[0] = (dp[0]*24 + dp[1]*23 + dp[2]*24 + dp[3]*23 + dp[4]*24) % MOD
        tmp[1] = (dp[0] + dp[1] + dp[2] + dp[3]) % MOD
        tmp[2] = dp[1]
        tmp[3] = (dp[0] + dp[1] + dp[3] + dp[4]) % MOD
        tmp[4] = dp[3]
        dp = tmp
    reder = sum(dp) % MOD

    return (der - reder) % MOD

print(solve())
    