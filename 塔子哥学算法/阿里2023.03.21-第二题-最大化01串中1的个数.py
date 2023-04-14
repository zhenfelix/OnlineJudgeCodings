
# 2023.03.21-第二题-最大化01串中1的个数
# 题目内容

# 曾经有一个小镇，镇上的居民都信奉一位神秘的数学家。这位数学家声名远扬，因为他曾经提出了一个关于二进制串的问题，而这个问题一直困扰着小镇上的居民。问题如下：

# 有一串由0和1组成的字符串，现在可以进行若干次如下操作：选择两个相邻的字符，将它们同时取反。例如，可以将00变成11，也可以将10变成01。请你求出最大化1字符数量的最小操作次数。
# 输入描述

# 一个长度不超过200000200000的、仅由’1'和’0组成的字符串。
# 输出描述

# 一个整数，代表最小的操作次数。
# 样例11

# 输入

# 0101

# 输出

# 2

# 说明 0101->0011->1111
# 样例22

# 输入

# 101

# 输出

# 0

# 说明 无论怎么操作，1的数量最大值也只能是2，因此无需操作。

from math import *
s = input()
n = len(s)
def check(ss):
    ones, flag = 0, 0
    dp = [0]*n 
    f = [0]*n 
    for i, ch in enumerate(ss):
        if ch == '0':
            flag ^= 1
        else:
            ones += flag
        f[i] = flag
        dp[i] = ones
    return dp, f 

ldp, lf = check(s)
rdp, rf = check(s[::-1])
rdp = rdp[::-1]
rf = rf[::-1]
tot = s.count('0')
if tot&1 == 0:
    print(tot//2+ldp[-1])
else:
    ans = inf 
    ldp.append(0)
    lf.append(0)
    rdp.append(0)
    rf.append(0)
    for i in range(n):
        if s[i] == '1': continue
        if lf[i-1] == 0 and rf[i+1] == 0:
            ans = min(ans,tot//2+ldp[i-1]+rdp[i+1])
    print(ans)












