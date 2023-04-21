# 题目内容

# 曾经有一个叫做塔子哥的年轻人，他是一个热衷于研究二叉树的数学家。他认为，一棵树只有当它的红色节点数量大于蓝色节点数量时才是好树。他的定义引起了人们的热议，有些人同意他的定义，有些人则持不同意见。但无论怎样，这个定义还是被广泛地接受了。

# 有一天，塔子哥发现了一棵好树，但他觉得它不够完美。于是他开始思考，如果能够将这棵好树分成两个好树，那它就更加完美了。

# 经过一番研究，他发现只需要删除一条边，就可以将这棵树分成两个好树。他想知道有多少种删除边的方案，于是他向你求助。
# 输入描述

# 第一行输入一个正整数 nn ，代表节点的数量。

# 第二行输入一个长度为 nn 的，仅包含 'R' 和 'B' 两种字符的字符串，第 ii 个字符为 'R' 代表第 ii 个节点被染成红色，'B'代表被染成蓝色。

# 接下来的 n−1n−1 行，每行输入两个正整数 uu 和 vv ，代表节点 uu 和节点 vv 有一条边连接。

# 1≤n≤1051≤n≤105
# 输出描述

# 一个整数，代表删边的方案数。
# 样例

# 输入

# 5
# RRBRB
# 1 2
# 2 3
# 1 4
# 4 5

# 输出

# 0

# 样例解释

# 无论删除哪条边，都会导致有一个子树不是好树。

from collections import *
n=int(input())
s = input()
g = defaultdict(list)
for _ in range(n-1):
    u, v = list(map(int,input().split()))
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

ans = 0
cc = Counter(s)
tr,tb = cc['R'],cc['B']
def dfs(cur,pre):
    global ans 
    r,b = 0,0
    if s[cur] == 'R':
        r += 1
    else:
        b += 1
    for nxt in g[cur]:
        if nxt == pre: continue
        nr,nb = dfs(nxt,cur)
        if nr > nb and tr-nr > tb-nb:
            ans += 1
        r += nr 
        b += nb 
    return r,b 
dfs(0,0)
print(ans)