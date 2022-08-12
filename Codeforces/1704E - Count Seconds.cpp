
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

#define DEBUG 0

using namespace std;
using ll = long long;
using pii = pair<int, int>;
using tiii = tuple<int,int,int>;
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 300005+50;
const int maxch = 26;
const int maxm = 20;

int t, n, m, x, y, c, q, k, pre, cur, last;
ll arr[maxn];
int degree[maxn], traversal[maxn];
vector<int> g[maxn];
ll MOD = 998244353, _clock;

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

template<class T>
void debug_arr(T a[], int start, int end){
    if (!DEBUG) return;
    for (int i = start; i <= end; i++) cout << a[i] << " ";
    cout << endl;
}

void topological(){
    queue<int> que;
    int idx = 0;
    for (int i = 1; i <= n; i++)
        if (degree[i] == 0)
            que.push(i);
    while (!que.empty())
    {
        int cur = que.front();
        traversal[idx++] = cur;
        que.pop();
        for (auto nxt : g[cur]){
            degree[nxt]--;
            if (degree[nxt] == 0)
                que.push(nxt);
        }
    }
}

ll solve()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++){
        scanf("%lld", &arr[i]);
        degree[i] = 0;
        g[i].clear();
    }
    for (int i = 0; i < m; i++){
        scanf("%d%d", &x, &y);
        degree[y]++;
        g[x].push_back(y);
    }
    debug_arr<vector<int>> (g, 1, n);
    topological();
    debug_arr<int>(traversal, 0, n-1);
    for (int i = 0; i < n; i++){
        bool flag = false;
        debug_arr<ll>(arr, 1, n);
        for (int j = n-1; j >= 0; j--){
            int cur = traversal[j];
            if (arr[cur]){
                flag = true;
                arr[cur]--;
                for (auto nxt : g[cur]) arr[nxt]++;
            }
        }
        if (!flag) return i;
    }
    ll ans = 0;
    for (int i = 0; i < n; i++){
        int cur = traversal[i];
        ans = arr[cur];
        for (auto nxt : g[cur])
            arr[nxt] = (arr[nxt] + arr[cur]) % MOD;
    }
    return (ans+n)%MOD;
}



int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    for (int i = 1; i <= t; i++) {
       printf("%lld\n", solve());
    }

}
