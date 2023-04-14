
# 2023.04.04-研发岗-第二题-子树
# 题目内容

# 塔子哥是一位研究生，他正在进行一项研究，研究的对象是一棵有根树。这棵树是他的导师从一个古老的图书馆里找到的，据说是一位著名学者曾经研究过的。树的根节点是1号节点，每个节点都有一个唯一的父节点。塔子哥花费了数周时间来研究这棵树，他终于了解了这棵树的结构和性质。

# 在研究过程中，塔子哥发现树上有一些特殊的节点，这些节点被染成了红色。他想知道有多少个子树包含了所有红色节点。
# 输入描述

# 第一行输入一个正整数 nn ，代表节点的数量。

# 第二行输入一个长度为 nn 的字符串，第 ii 个字符为 'R' 代表第 ii 个节点被染成红色，为 'W' 代表未被染色。

# 接下来的 n−1n−1 行，每行输入两个正整数 xx 和 yy ，代表 xx 和 yy 有一 条边连接。

# 1≤n≤1051≤n≤105

# 1≤x,y≤n1≤x,y≤n
# 输出描述

# 输出有多少子树满足子树所有节点均为红色。
# 样例

# 输入

# 3
# WRR
# 1 2
# 1 3

# 输出

# 2


from collections import * 
n=int(input())
color=input() 
g=defaultdict(list)
for _ in range(n-1):
    x,y=list(map(int,input().split()))
    x-=1
    y-=1
    g[x].append(y)
    g[y].append(x)

ans = 0
def dfs(cur,parent):
    global ans 
    cnt, r = 1, 0
    if color[cur] == 'R': r += 1
    for nxt in g[cur]:
        if nxt == parent: continue
        ncnt,nr = dfs(nxt,cur)
        cnt += ncnt
        r += nr 
    if cnt == r: ans += 1 
    return cnt, r 
dfs(0,0)
print(ans)
