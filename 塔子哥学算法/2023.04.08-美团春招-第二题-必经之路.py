
# 2023.04.08-美团春招-第二题-必经之路
# 题目内容

# 塔子哥的班主任最近组织了一次户外拓展活动，让班里的同学们一起去爬山。在路上，塔子哥看到了一棵漂亮的树，他对这棵树产生了浓厚的兴趣，开始观察并记录这棵树的一些特征。

# 塔子哥发现这棵树有 nn 个节点，其中有一条边被特别标记了出来。他开始思考这条特殊的边在树上起到了什么样的作用，于是他想知道，经过这条选定边的所有树上简单路径中，最长的那条路径有多长，以便更好地理解这棵树的结构。

# 一条简单的路径的长度指这条简单路径上的边的个数。
# 输入描述

# 第一行一个整数 nn ，表示树的节点个数。

# 第二行 n−1n−1 个整数，第 ii 个数 pipi​ 表示节点 i+1i+1 和 pipi​ 之间有一条边相连。

# 第三行两个整数 xx ， yy ，表示这条选定的边。保证这条边一定是树上的一条边。

# 对于全部数据， 2≤n≤1052≤n≤105 ， 1≤pi≤n1≤pi​≤n ， 1≤x,y≤n1≤x,y≤n ， x≠yx=y 。

# 保证输入数据正确描述一棵树，并且( x,yx,y ) 是树上的条边。
# 输出描述

# 输出一行，一个整数，表示所有经过选定边的树上简单路径中，最长的那条的长度。
# 样例

# 输入

# 7
# 1 2 3 4 5 3
# 3 7

# 输出

# 4


from collections import *
n = int(input())
arr = list(map(int,input().split()))
g = defaultdict(list)
for i in range(n-1):
    u = i+1
    v = arr[i]-1
    g[u].append(v)
    g[v].append(u)
x, y = list(map(int,input().split()))
x -= 1
y -= 1
visited = [0]*n 

def dfs(cur,parent):
    depth = 0
    for nxt in g[cur]:
        if nxt == parent: continue
        depth = max(depth,1+dfs(nxt,cur))
    return depth

print(dfs(x,y)+dfs(y,x)+1)
    from collections import *
n = int(input())
arr = list(map(int,input().split()))
g = defaultdict(list)
for i in range(n-1):
    u = i+1
    v = arr[i]-1
    g[u].append(v)
    g[v].append(u)
x, y = list(map(int,input().split()))
x -= 1
y -= 1
visited = [0]*n 

def dfs(cur,parent):
    depth = 0
    for nxt in g[cur]:
        if nxt == parent: continue
        depth = max(depth,1+dfs(nxt,cur))
    return depth

print(dfs(x,y)+dfs(y,x)+1)
    