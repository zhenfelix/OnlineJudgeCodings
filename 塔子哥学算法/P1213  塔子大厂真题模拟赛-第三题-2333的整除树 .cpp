// 题目内容

// 2333 构造了一个与数论相关的树。这棵树上的每一个节点都有一个权值wiwi​.

// 一个点对(u,v)(u,v) 被称作"X-整除"的，当且仅当它们的所有公共祖先都能够被某个数XX整除。

//     xx的祖先:从节点xx到树的根经过的所有节点为该节点的祖先。 xx,yy的公共祖先:既是xx的祖先，又是yy的祖先的结点。

// 现在2333有 qq 次询问，每次问你这颗树上的两个点是否是"X-整除"的。但是他转而向你求助。请你帮帮他吧!
// 输入描述

// 第一行一个整数 nn , 代表这棵树的节点的个数。

// 第二行 n−1n−1 个整数 , f2,f3,...,fnf2​,f3​,...,fn​ 分别代表这些点的父亲节点,根为1。

// 第三行 nn 个整数, w1,w2,...,wnw1​,w2​,...,wn​ ,分别代表每个点的权值。

// 第四行一个整数 qq ,代表询问次数。

// 接下来 qq 行,每行三个数 u v xu v x 代表询问。
// 数据范围

// 1≤n≤1e41≤n≤1e4

// 1≤fi≤n1≤fi​≤n , 保证给定的是一颗合法的树。

// 1≤wi≤1e91≤wi​≤1e9

// 1≤q≤5001≤q≤500

// 1≤u,v≤n1≤u,v≤n

// 1≤x≤1e91≤x≤1e9
// 输出描述

// 输出 qq 个数,代表每次的询问结果：若其是"X-整除"的,则输出 YESYES , 否则输出 NONO 。注意YES， NO必须大写，其他写法不得分
// 样例1

// 输入

// 5
// 1 1 3 3
// 8 6 4 8 3
// 4
// 1 3 4
// 1 3 9
// 4 5 4
// 4 5 8

// 输出

// YES
// NO
// YES
// NO

// 样例解释:

// 第一次询问 : 1,31,3的公共祖先为11 , 值为88 , 能够被44 整除,所以输出YESYES

// 第二次询问 : 1,31,3的公共祖先为11 , 值为88 , 不能被99 整除,所以输出NONO

// 第三次询问 : 4,54,5的公共祖先为1,31,3 , 值为8,48,4 , 都能够被44 整除,所以输出YESYES

// 第四次询问 : 4,54,5的公共祖先为1,31,3 , 值为8,48,4 , 结点33不能被88 整除,所以输出NONO
// bonus(2个测试点)

// 1≤n≤1e51≤n≤1e5

// 1≤fi≤n1≤fi​≤n , 保证给定的是一颗合法的树。

// 1≤wi≤1e91≤wi​≤1e9

// 1≤q≤1e51≤q≤1e5

// 1≤u,v≤n1≤u,v≤n

// 1≤x≤1e91≤x≤1e9




#include <bits/stdc++.h>
#include <functional>
#include <vector>
using namespace std;
using pii = pair<int,int>;
using tiii = tuple<int,int,int>;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    // freopen("contests/input","r",stdin);
    int n;
    cin >> n;
    vector<int> father(n,0);
    vector<vector<int>> g(n);
    for (int i = 1; i < n; i++) {
        int p;
        cin >> p;
        father[i] = p-1;
        g[father[i]].push_back(i);
    }
    vector<int> weights(n,0);
    for (int i = 0; i < n; i++) cin >> weights[i];
    function<void(int,int)> dfs = [&] (int cur, int p) {
        weights[cur] = gcd(weights[cur], weights[p]);
        for (auto nxt : g[cur]) {
            if (nxt == p) continue;
            dfs(nxt,cur);
        }
    };
    dfs(0,0);
    int q;
    cin >> q;
    vector<vector<tiii>> qs(n);
    for (int i = 0; i < q; i++) {
        int u, v, x;
        cin >> u >> v >> x;
        u--;v--;
        qs[u].push_back({v,i,x});
        qs[v].push_back({u,i,x});
    }
    vector<int> parent(n);
    for (int i = 0; i < n; i++) parent[i] = i;
    function<int(int)> find = [&] (int cur) {
        return parent[cur] == cur ? cur : find(parent[cur]);
    };
    vector<int> ans(q,0);
    vector<int> visited(n,0);
    function<void(int,int)> dfs2 = [&] (int cur, int p) {
        visited[cur] = 1;
        for (auto [v,i,x] : qs[cur]) {
            // cout << cur << ' ' << v << ' ' << find(v) << endl;
            if (visited[v] && weights[find(v)]%x == 0) ans[i] = 1;
        }
        for (auto nxt : g[cur]) {
            if (nxt == p) continue;
            dfs2(nxt, cur);
        }
        parent[cur] = father[cur];
    };
    dfs2(0,0);
    for (int i = 0; i < q; i++) {
        if (ans[i] == 1) cout << "YES";
        else cout << "NO";
        cout << endl;
    }
    return 0;

}