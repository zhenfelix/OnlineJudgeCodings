
// 2023.03.21-第二题-红白染色树
// 题目内容

// 曾经有一个名叫塔子哥的年轻人，他喜欢探索和解决各种难题。有一天，他发现了一棵神奇的树。树上已经有一些点被染成了红色，另一些点被染成了白色。

// 但是塔子哥想让相邻的两个点不能够颜色相同，因此他想知道最少需要进行多少次操作才能让树上所有相邻两个点的颜色不同，每次操作塔子哥可以选择一个点改变它的染色状态（红色变白色或者白色变红色）。

// 这个问题困扰着他很长一段时间，但是他决定不放弃，你能帮塔子哥想一想怎么解决这个问题吗？
// 输入描述

// 第一行输入一个正整数 nn ，代表节点的数量。

// 第二行输入一个长度为 nn 的、仅由 'R' 、 'W' 两种字符组成的字符串，第 ii 个字符为 'R' 代表 ii 号节点被染成红色， 'W' 代表被染成白色。

// 接下来的 n−1n−1 行，每行输入两个正整数 uu 和 vv ，代表节点 uu 和节点 vv 有一条路径相连。

// 1≤n≤1051≤n≤105

// 1≤u,v≤n1≤u,v≤n
// 输出描述

// 一个整数，代表最小的操作次数。
// 样例

// 输入

// 5
// RRWWR
// 1 2
// 1 3
// 2 4
// 4 5

// 输出

// 2

// 样例解释

// 对 11 号和 33 号节点各操作一次即可。

#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<vector<int>> g(n);
    for (int i = 0; i < n-1; i++) {
        int u, v;
        cin >> u >> v;
        u--;v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    vector<int> color(n);
    function<void(int,int,int)> dfs = [&] (int cur, int pre, int mark) {
        color[cur] = mark;
        for (auto nxt : g[cur]) {
            if (nxt == pre) continue;
            dfs(nxt,cur,mark^1);
        }
    };
    dfs(0,0,0);
    vector<vector<int>> cnt(2,vector<int>(2,0));
    for (int i = 0; i < n; i++) {
        int x = color[i];
        int y = s[i] == 'R' ? 0 : 1;
        cnt[x][y]++;
    }
    int ans = min(cnt[0][0]+cnt[1][1],cnt[0][1]+cnt[1][0]);
    cout << ans << endl;
    return 0;
}