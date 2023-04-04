
// 2023.03.28-第三题-塔子的有根树
// 题目内容

// 塔子哥拿到了一棵有根树，ii号节点的权值为valivali​。我们规定11号点为这棵树的根节点。接着，塔子哥被给出qq次操作，每次操作会选择一个节点tt，使得以uu为根的子树上的所有节点的权值都乘上一个gg。

// 塔子哥想知道，在qq次操作结束以后对于所有点而言，以节点ii为根的子树的所有点的权值的乘积末尾有多少个0?
// 输入描述

// 第一行输入一个正整数nn，代表这颗树的节点的数量。

// 第二行输入nn个正整数valivali​，代表每个节点的权值。

// 接下来的n−1n−1行，每行输入两个正整数uu和vv，代表节点uu和节点vv有一条边相连。

// 接下来的一行输入一个正整数qq，代表操作次数。

// 接下来的qq行，每行输入两个正整数tt和gg，代表塔子哥的一次操作。

// 1⩽n,q⩽1051⩽n,q⩽105

// 1⩽vi,g⩽1091⩽vi​,g⩽109

// 1⩽t,u,v⩽n1⩽t,u,v⩽n
// 输出描述

// 输出一行nn个正整数，分别代表1号节点到nn号节点，每个节点的子树权值乘积尾零的数量。
// 样例

// 输入

// 5
// 2 2 2 5 5
// 1 2
// 1 3
// 2 4
// 2 5
// 1
// 2 10

// 输出

// 5 4 0 1 1

// *说明*

// 操作后2号、4号、5号节点都乘以5，每个节点的权值分别是[2, 20, 2, 50, 50]

// 1号节点为根的子树乘积是200000，未尾有5个0。

// 2号节点为根的子树乘积是50000， 末尾有4个0。

// 4号节点为根的子树乘积是50， 末尾有1个0。

// 5号节点为根的子树乘积是50， 末尾有1个0。


#include<bits/stdc++.h>

using namespace std;
using pii = pair<int,int>;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    // freopen("contests/input","r",stdin);
    int n,a,t,g,q,u,v;
    cin >> n;
    vector<vector<int>> graph(n);
    vector<vector<int>> cnt(n,vector<int>(2)),qs(n,vector<int>(2));
    vector<int> cc(n,1);
    function<pii(int)> calc = [&](int a) -> pii
    {
        int x = 0, y = 0;
        while (a%2 == 0)
        {
            a /= 2;
            x++;
        }
        while (a%5 == 0)
        {
            a /= 5;
            y++;
        }
        return {x,y};
    };
    for (int i = 0; i < n; i++) {
        cin >> a;
        auto [x,y] = calc(a);
        cnt[i][0] += x;
        cnt[i][1] += y;
    }
    for (int i = 0; i < n-1; i++){
        cin >> u >> v;
        graph[u-1].push_back(v-1);
        graph[v-1].push_back(u-1);
    }
    cin >> q;
    for (int i = 0; i < q; i++){
        cin >> t >> g;
        auto [x,y] = calc(g);
        qs[t-1][0] += x;
        qs[t-1][1] += y;
    }
    function<void(int,int,int,int)> dfs = [&] (int cur, int parent, int x, int y){
        x += qs[cur][0];
        y += qs[cur][1];
        cnt[cur][0] += x;
        cnt[cur][1] += y;
        for (auto nxt : graph[cur]){
            if (nxt == parent) continue;
            dfs(nxt,cur,x,y);
            cc[cur] += cc[nxt];
            cnt[cur][0] += (cnt[nxt][0]);
            cnt[cur][1] += (cnt[nxt][1]);
        }
        return;
    };
    dfs(0,0,0,0);
    for (int i = 0; i < n; i++){
        cout << min(cnt[i][0],cnt[i][1]);
        if (i < n-1) cout << ' ';
    }
    cout << endl;
}