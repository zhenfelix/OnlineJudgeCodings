
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
ll MOD = 998244353;

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

void solve()
{
    scanf("%d%d", &n, &m);
    ll val;
    for (int i = 1; i <= n; i++){
        arr[i] = 0;
        traversal[i] = i;
        for (int j = 1; j <= m; j++){
            scanf("%lld", &val);
            arr[i] += j*val;
        }
    }
    sort(traversal+1, traversal+n+1, [&](int a, int b){return arr[a] < arr[b];});
    printf("%d %lld\n", traversal[n], arr[traversal[n]]-arr[traversal[n-1]]);
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
