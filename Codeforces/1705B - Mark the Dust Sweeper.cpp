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
using pci = pair<char, int>;

const int inf = 0x3f3f3f3f;
const int maxn = 200005;
const int maxch = 26;

int t, n, m, x, y;
// int a[maxn], b[maxn], idx[maxn], lo[maxn], hi[maxn];
ll u[maxn];
ll p;
string s;
ll cnt[maxch];
// ll s[maxn], mx;

std::ostream &operator<<(std::ostream &stream,
                         vector<pci> &v)
{
    for (auto [ch,i] : v) stream << ch << ": " << i << " ";
    return stream;
}


void solve()
{
    scanf("%d\n", &n);
    for (int i = 0; i < n; i++) scanf("%lld", &u[i]);
    ll ans = 0;
    int j = 0;
    for (int i = 0; i < n-1; i++){
        j = max(j,i);
        while (u[i] > 0 && j < n-1)
        {
            while (u[j] > 0 && j < n-1) j++;
            u[i]--;u[j]++;ans++;
        }
        ans += u[i];
    }
    printf("%lld\n", ans);
    return;
}

int main()
{
    // freopen("input", "r", stdin);
    scanf("%d\n", &t);
    // for(int i = 0; i < t; i++){
    //     if (solve()){
    //         printf("YES\n");
    //     }
    //     else{
    //         printf("NO\n");
    //     }
    // }
    for (int i = 0; i < t; i++)
    {
        solve();
    }
}