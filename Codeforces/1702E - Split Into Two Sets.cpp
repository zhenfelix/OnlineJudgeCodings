
// #include <bits/stdc++.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <climits>
#include <iostream>
#include <unordered_map>
#include <cstring>
#include <queue>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005;
const int maxch = 26;

int t, n, m, x, y;
// int a[maxn], b[maxn], idx[maxn], lo[maxn], hi[maxn];
// ll u[maxn];
ll p;
string s;
ll cnt[maxch];
// ll s[maxn], mx;

int dfs(int cur, vector<vector<int>> &g, vector<bool> &visited){
    visited[cur] = true;
    int cc = 1;
    for (auto nxt : g[cur]){
        if (!visited[nxt]) cc += dfs(nxt, g, visited);
    }
    return cc;
}

bool solve()
{
    scanf("%d\n", &n);
    map<int,vector<int>> mp;
    // vector<pii> arr;
    // bool flag = true;
    for (int i = 0; i < n; i++){
        scanf("%d%d", &x, &y);
        // x--;
        // y--;
        // arr.push_back({x,y});
        mp[x].push_back(i);
        mp[y].push_back(i);
        // if (mp[x].size() > 2 || mp[x].size() > 2 || x == y){
        //     flag = false;
        // }
    }
    // if (!flag) return false;
    vector<vector<int>> g(n);
    for (auto [v, ij] : mp){
        if (ij.size() != 2) return false;
        int i = ij[0], j = ij[1];
        if (i == j) return false;
        g[i].push_back(j);
        g[j].push_back(i);
    }
    vector<bool> visited(n, false);
    for (int i = 0; i < n; i++){
        if (!visited[i]){
            int cnt = dfs(i, g, visited);
            if (cnt%2 == 1) return false;
        }
    }
    return true;
    
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for(int i = 0; i < t; i++){
        if (solve()){
            printf("YES\n");
        }
        else{
            printf("NO\n");
        }
    }
}
