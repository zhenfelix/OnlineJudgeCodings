
// 2023.3.16-二维矩阵可传送的最短路
// 题目内容

// 塔子哥是一名冒险家，经过了漫长的旅途，他终于到达了传说中的神秘迷宫。在迷宫里，塔子哥发现了一张 nn 行 mm 列的二维矩阵，矩阵的每个元素都代表着一个位置，同时每个位置还对应着一个花费值。这个花费值代表着从当前位置走到下一个位置需要消耗的时间。塔子哥站在矩阵的左上角，他每一步可以走上、下、左、右四种方向中的一个，花费的时间为这两个相邻元素的差的绝对值。

// 此时，塔子哥已经花费了很多时间在迷宫中行走，而他又发现了一件奇怪的事情，就是在这个迷宫中存在传送阵。这个传送阵可以让他瞬间从一个位置传送到另一个位置，而且不会消耗任何时间。不过这个传送阵有两个个限制，这个传送阵只能使用一次，并且只能从一个数字到达另一个相同的数字。这就意味着，如果他想要使用这个传送阵，他需要在同一个数字出现两次之后，才能将这个数字作为传送阵的起点或终点。

// 为了尽快走出这个迷宫，塔子哥想知道，从左上角走到右下角最少需要多少时间。
// 输入描述

// 第一行输入两个正整数 nn 和 mm 。代表矩阵的行和列。

// 接下来的 nn 行，每行输入 mm 个正整数 aijaij​ ，代表矩阵的元素

// 1≤n,m≤5001≤n,m≤500

// 1≤aij≤1091≤aij​≤109
// 输出描述

// 一个整数，代表最少需要花费的时间。
// 样例11

// 输入

// 3 3
// 1 3 5
// 2 1 4
// 2 5 6

// 输出

// 5


#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int,int>;
using tlii = tuple<ll,int,int>;
int main() {
    int n,m;
    cin >> n >> m;
    vector<vector<int>> mat(n,vector<int>(m));
    unordered_map<int, ll> dist,rdist;
    unordered_map<int, vector<pii>> g;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> mat[i][j];
            int v = mat[i][j];
            g[v].push_back({i,j});
            dist[v] = LLONG_MAX;
            rdist[v] = LLONG_MAX;
        }
    }
    function<void(int,int,unordered_map<int, ll> &)> calc = [&] (int i, int j, unordered_map<int, ll> &dist_tmp) {
        vector<vector<ll>> dp(n,vector<ll>(m,LLONG_MAX));
        dp[i][j] = 0;
        priority_queue<tlii,vector<tlii>,greater<>> pq;
        pq.push({0,i,j});
        vector<pii> dxy {{-1,0},{1,0},{0,-1},{0,1}};
        while (!pq.empty()) {
            auto [d,x,y] = pq.top();
            pq.pop();
            int v = mat[x][y];
            if (d > dp[x][y]) continue;
            dist_tmp[v] = min(dist_tmp[v],d);
            for (auto [dx,dy] : dxy) {
                dx += x;
                dy += y;
                if (dx >= 0 && dx < n && dy >= 0 && 
            dy < m) {
                    ll w = mat[dx][dy];
                    ll nd = d + abs(w-v);
                    if (nd < dp[dx][dy]) {
                        pq.push({nd,dx,dy});
                        dp[dx][dy] = nd;
                    }
                }
            }   
 
        }
        return;
    };
    calc(0,0,dist);
    calc(n-1,m-1,rdist);
    ll ans = LLONG_MAX;
    for (auto [v,d] : dist) {
        ans = min(ans, d+rdist[v]);
    }
    cout << ans;
    return 0;
}