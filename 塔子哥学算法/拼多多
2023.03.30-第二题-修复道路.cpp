
// 2023.03.30-第二题-修复道路
// 题目内容

// 在这座树形城市中，有 nn 个节点互相连接，每个节点可以作为一座城市的代表。塔子哥是这座城市的管理员，他一直关注着这座城市的安全和交通状况。

// 但是最近，城市中的一些道路因为年久失修、自然灾害等原因出现了断裂，这导致了交通的瘫痪和城市的分裂。为了解决这个问题，塔子哥决定组织一支维修队来修复这些断裂的道路。

// 维修队会从城市中的出发点 11 出发，一个维修队从 11 出发到一个点，路上所有断边都会被修好。

// 塔子哥想知道最少需要多少个维修队，才能修复好整座城市的断边。
// 输入描述

// 输入第一行为一个整数 nn ，（ 1≤n≤1051≤n≤105 ）

// 接下来 nn 行，每一行有三个整数， u,v,zu,v,z ， z=1z=1 代表 uu 到 vv 的边为断的， z=0z=0 代表 uu 到 vv 的边是好的。
// 输出描述

// 输出最少需要多少个修理队，能修复好整座城市的断边。
// 样例1

// 输入

// 4
// 1 2 0
// 1 3 1
// 2 4 0

// 输出

// 1

// 样例2

// 输入

// 5
// 1 2 1
// 1 3 0
// 2 5 1
// 3 4 1

// 输出

// 2



#include<bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int,int>;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  // freopen("contests/input","r",stdin);
  int n;
  cin >> n;
  vector<vector<pii>> graph(n);
  for (int i = 0; i < n-1; i++) {
    int u,v,s;
    cin >> u >> v >> s;
    u--;v--;
    graph[u].push_back({v,s});
    graph[v].push_back({u,s});
  }
  function<int(int,int)> dfs = [&] (int cur,int parent) {
    int cnt = 0;
    for (auto &[nxt,s] : graph[cur]) {
      if (nxt == parent) continue;
      int tmp = dfs(nxt,cur);
      cnt += s == 0 ? tmp : max(tmp,1);
    }
    return cnt;
  };
  cout << dfs(0,0) << endl;
}