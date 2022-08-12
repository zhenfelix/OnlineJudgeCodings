
#include <bits/stdc++.h>
// #include <vector>
// #include <set>
// #include <map>
// #include <algorithm>
// #include <climits>
// #include <iostream>
// #include <unordered_map>
// #include <cstring>
// #include <queue>

#define DEBUG 0

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using tiii = tuple<int,int,int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005+50;
const int maxch = 26;
const int maxm = 110;

int t, n, m, x, y, c, p, q, k, last, s;
ll MOD = 998244353;

vector<tiii> g[maxn];
int cnt[maxn];


std::ostream &operator<<(std::ostream &stream,
                         vector<pii> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}

std::ostream &operator<<(std::ostream &stream,
                         vector<int> &v)
{
    for (auto x : v)
        stream << x << "-";
    return stream;
}

std::ostream &operator<<(std::ostream &stream,
                         vector<ll> &v)
{
    for (auto x : v)
        stream << x << "-";
    return stream;
}

template<class T>
void debug_arr(T a[], int start, int end){
    if (!DEBUG) return;
    for (int i = start; i <= end; i++) cout << a[i] << " ";
    cout << endl;
}

bool myless(string a, string b){
    return a.length() < b.length() || (a.length() == b.length() && a < b);
}

void dfs(int cur, int pre, ll sums, vector<ll> &vb){
    // cout << cur << " " << pre << endl;
    // cout << va << endl;
    // cout << vb << endl;
    cnt[cur] = upper_bound(vb.begin(), vb.end(), sums)-vb.begin()-1;
    for (auto [nxt, a, b] : g[cur]){
        vb.push_back(vb.back()+b);
        dfs(nxt,cur,sums+a,vb);
        vb.pop_back();
    }
    return;
}

void solve()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        g[i].clear();
        cnt[i] = 0;
    }
    for (int i = 2; i <= n; i++){
        scanf("%d%d%d", &p, &x, &y);
        g[p].push_back({i,x,y});
    }
    vector<ll> cost_a = {0}, cost_b = {0};
    dfs(1,1,0,cost_b);
    for (int i = 2; i <= n; i++){
        printf("%d", cnt[i]);
        if (i < n) printf(" ");
        else printf("\n");
    }
    return;
}



int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for (int i = 1; i <= t; i++) {
        solve();
    }

}
