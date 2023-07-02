# 题目描述

# 塔子哥最近接到一个游戏设计的工程，其中有 NN 个角色（分别编号 1 N1 N ）。

# 在游戏设定中，每个初始角色的战斗力用其等级高低来评价，每个初始角色都会有一个固定的等级。

# 为了设计一个完善的等级系统，塔子哥为这些初始角色设计了 MM 场战斗来测试这些初始角色的强度。如果战斗的角色等级相等，那么会出现平局；如果不同等级角色之间的战斗，高等级的角色一定会击败低等级角色。

# 塔子哥想知道应该为这些角色设计多少种等级数量 ansans ，如果战斗违反设定或者无法确定，那么就返回 ”-1“。
# 输入描述

# 输入第一行一个整数 TT ，代表测试用例的组数。(1≤T≤101≤T≤10)

# 接下来 TT 组测试数据，对于每一组测试用例，第一行两个整数 NN 和 MM ，分别代表角色的数量和战斗的场数。( 1≤N≤10000,1≤M≤200001≤N≤10000,1≤M≤20000) (可能存在重边)

# 接下来 MM 行，表示角色A和角色B的战斗结果( 1≤A,B≤N1≤A,B≤N )，有三种可能:

#     A>B，表示A击败了B;

#     A<B，表示A输给了B;

#     A=B，表示A和B打平;

# 输出描述

# 对于每组测试用例，如果战斗结果符合等级设定，输出总共的等级数量 ansans ; 否则输出-1，表示违反设定或无法确定。
# 样例

# 样例输入

# 5
# 4 3
# 1 < 2
# 2 < 3
# 3 = 4
# 4 3
# 1 < 2
# 2 > 3
# 3 = 4
# 5 5
# 1 < 1
# 1 < 2
# 2 < 3
# 3 < 4
# 4 < 5
# 7 6
# 1 < 2
# 2 < 3
# 3 < 4
# 4 < 5
# 5 < 6
# 6 = 7
# 8 6
# 1 = 2
# 2 = 4
# 5 = 4
# 6 = 7
# 7 = 8
# 5 = 6

# 样例输出

# 3
# -1
# -1
# 6
# -1

# 样例说明

# 第一组用例，由3和4的打平可以得出3和4处于同一等级，而3击败了2，2击败了1，因此有:{1}<{2}<{3,4}，共3种等级。

# 第二组用例，2击败了1，2又击败了3,但是无法确定1和3之间的等级关系，因此无法确定人物之间的等级。

# 第三组用例，1号自己输给自己，违反了相同等级不能分出胜负的设定。

# 第四组用例，有:{1}<{2}<{3}<{4}>{5}<{6,7}，共6种等级。

# 第五组用例，3没有任何战斗，无法确定其所在等级。

from collections import * 

t = int(input())

def solve():
    n, m = list(map(int,input().split()))
    parent = list(range(n)) 
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    def connect(u,v):
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv 
        return
    g = defaultdict(list)
    for _ in range(m):
        u,op,v = input().split()
        u = int(u)-1
        v = int(v)-1
        if op == '=':
            connect(u,v)
        elif op == '<':
            g[u].append(v)
        else:
            g[v].append(u)
    ng = [[] for _ in range(n)]
    degree = [0]*n 
    gp = [find(i) for i in range(n)]
    for k, arr in g.items():
        for a in arr:
            u, v = gp[k], gp[a]
            ng[u].append(v)
            degree[v] += 1
    q = []
    for i in range(n):
        if degree[i] == 0 and gp[i] == i:
            q.append(i)
    ans = 0
    while q:
        nq = []
        if len(q) > 1:
            return -1
        for cur in q:
            for nxt in ng[cur]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    nq.append(nxt)
        q = nq 
        ans += 1
    if any(degree[i] != 0 for i in range(n)):
        return -1
    return ans 

for _ in range(t):
    print(solve())