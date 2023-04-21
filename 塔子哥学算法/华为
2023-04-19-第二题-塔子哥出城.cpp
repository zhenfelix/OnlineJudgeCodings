
// 2023-04-19-第二题-塔子哥出城
// 题目内容

// 塔子哥居住在数据结构之城，如果将这个城市的路口看做点，两个路口之间的路看做边，那么该城市的道路能够构成一棵由市中心路口向城市四周生长的树，树的叶子节点即是出城口。

// 塔子哥今天想要出城办事，但不巧的是，有几个路口堵车了，塔子哥无法从一个正常的路口前往堵车的路口。假定塔子哥从一个正常的路口出发，请问塔子哥能否顺利出城（到达出城口）？如果可以，请帮塔子哥找到最省油的路径（经过路口最少的路径），否则请输出“NO”。
// 输入描述

// 第一行给出数字n，表示这个城市有n个路口，路口从0开始依次递增，0固定为根节点，1<=n<10000

// 第二行给出数字m，表示接下来有m行，每行是一条道路

// 接下来的m行是边: x，y，表示x和y路口有一条道路连接。保证是一颗树

// 道路信息结束后接下来的一行给出数d，表示接下菜有d行，每行是一个堵车的路口

// 接下来的d行是堵车路口k，表示路口k已堵车
// 输出描述

// 如果塔子哥能够顺利出城，请输出塔子哥能够到达任意一个出城口的最短路径（通过路口最少），比如塔子哥从0经过1到达2 (出城口) ，那么输出“0->1->2”;否则输出“NO”。注意如果存在多条最短路径，请按照节点序号排序输出，比如 0->1 和 0-> 3两条路径，第一个节点0一样，则比较第二个节点1和3，1比3小，因此输出0->1这条路径。再如0->5->2->3和 0->5->1->4，则输出 0->5->1->4。
// 样例
// 样例1

// 输入

// 4
// 3
// 0 1
// 0 2
// 0 3
// 2
// 2
// 3

// 输出

// 0->1

// 说明

// n=4, edge=[[0,1],[0,2], [0.3], block=[2, 3]] 表示一个有4个节点，3条边的树，其中节点2和节点3上有障碍物，小猴子都能从01到达叶子节点1（节点1只有一条边[0,1]和它连接，因此也是叶子节点），即可以跑出这个树，所以输出为0->1.
// 样例2

// 输入

// 7
// 6
// 0 1
// 0 3
// 1 2
// 3 4
// 1 5
// 5 6
// 1
// 4

// 输出

// 0->1->2

// 说明

// 节点4上有障碍物，因此0-3-4这条路不通，节点2和节点6都是叶子节点，但0->1->2比0->1->5->6路径短 (通过的边最少) ，因此输出为0->1->2。

#include <bits/stdc++.h>
#include <ios>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    cin >> n;
    vector<vector<int>> g(n,vector<int>());
    cin >> m;
    while (m--) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    int d;
    cin >> d;
    vector<int> block(n,0);
    while (d--) {
        int x;
        cin >> x;
        block[x] = 1;
    }
    vector<int> parent(n,-1); 
    vector<int> ans {n+1,-1};
    function<void(int,int,int)> dfs = [&] (int cur, int pre, int depth) {
        if (block[cur]) return;
        parent[cur] = pre;
        sort(g[cur].begin(),g[cur].end());
        for (auto nxt : g[cur]) {
            if (nxt == pre) continue;
            dfs(nxt,cur,depth+1);
        }
        if (g[cur].size() == 1) {
            if (depth < ans[0]) ans = {depth,cur};
        }
        return;
    };
    dfs(0,-1,0);
    if (ans[1] == -1) cout << "NULL\n";
    else {
        vector<int> path;
        int cur = ans[1];
        while (cur != -1) {
            path.push_back(cur);
            cur = parent[cur];
        }
        while (!path.empty()) {
            cout << path.back();
            path.pop_back();
            if (!path.empty()) cout << "->";
        }
    }
    return 0;
}