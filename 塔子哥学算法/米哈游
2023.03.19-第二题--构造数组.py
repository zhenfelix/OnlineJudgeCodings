
# 2023.03.19-第二题--构造数组
# 题目内容

# 在一个小镇上，有一个富有的商人，他名叫塔子哥。他一直很自豪地说自己是一个数学家，但是他很长一段时间都没有找到一些有趣的问题来解决。终于有一天，他遇到了一个叫做朱莉的年轻女子。她向他提出了这个问题：

# “我想找一个数组，它满足所有元素的绝对值不大于 33 ，任意相邻的两个元素的乘积小于 00 ，且它们的和不为 00 ，并且所有元素之和等于 00 。你能帮我找到这样一个数组吗？”

# 塔子哥开始思考这个问题。他试图通过手算一些例子来找出一个通用的方法。但是，他发现这个问题实际上非常困难，他不知道该如何开始解决它，你能帮塔子哥解决这个问题吗？
# 输入描述

# 一个正整数 nn 。 2≤n≤1052≤n≤105
# 输出描述

# 如果无解，请输出一个字符串 No Answer 。

# 否则输出 nn 个整数。有多解输出任意即可。
# 样例
# 样例一

# 输入

# 2

# 输出

# No Answer

# 样例二

# 输入

# 3

# 输出

# -1 2 -1

# 样例解释

# 输出 2 -3 1 等合法解也是可以的。

n=int(input())
if n < 3:
    print("No Answer")
elif n == 3:
    print("-1 3 -2")
else:
    base = [-1, 3, -2, 1, -3, 2]
    s = [[1, -3, 2, -1, 3, -2],[1, -2, 3, -2],[1, -3, 1, -2, 3]]
    m = n//6
    ans = base*m 
    r = n%6
    if r:
        if r <= 3:
            ans = ans[:-3]
        else:
            ans = s[0]*m 
        r %= 3
        ans += s[r]
    print(*ans)